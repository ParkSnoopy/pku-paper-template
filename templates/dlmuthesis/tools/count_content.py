#!/usr/bin/env python3
"""Count Chinese, English, and punctuation characters in paper content."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

INPUT_PATTERN = re.compile(r"\\(?:input|include)\s*\{([^{}]+)\}")
BODY_START_PATTERN = re.compile(r"\\pesudohookOFpremainbody\b")
BODY_END_PATTERN = re.compile(r"\\input\s*\{references(?:\.tex)?\}")

DISCARD_ARGUMENTS = {
    "bibitem": 1,
    "cite": 1,
    "citep": 1,
    "citet": 1,
    "eqref": 1,
    "includegraphics": 1,
    "label": 1,
    "pageref": 1,
    "ref": 1,
    "upcite": 1,
}
VISIBLE_COMMANDS = {
    "LaTeX": "LaTeX",
    "TeX": "TeX",
    "dots": "…",
    "ldots": "…",
    "textbackslash": "\\",
    "textemdash": "—",
    "textendash": "–",
    "textgreater": ">",
    "textless": "<",
}
ESCAPED_CHARACTERS = {"#", "$", "%", "&", "_", "{", "}"}
VERBATIM_ENVIRONMENTS = {"Verbatim", "lstlisting", "minted", "verbatim"}
ENVIRONMENT_ARGUMENTS = {
    "minipage": 1,
    "multicols": 1,
    "tabular": 1,
    "tabular*": 2,
    "tabularx": 2,
    "thebibliography": 1,
}


@dataclass(frozen=True)
class Counts:
    chinese: int = 0
    english: int = 0
    punctuation: int = 0

    @property
    def total(self) -> int:
        return self.chinese + self.english + self.punctuation

    def __add__(self, other: "Counts") -> "Counts":
        return Counts(
            self.chinese + other.chinese,
            self.english + other.english,
            self.punctuation + other.punctuation,
        )


def remove_comments(source: str) -> str:
    lines: list[str] = []
    for line in source.splitlines(keepends=True):
        index = 0
        while True:
            index = line.find("%", index)
            if index < 0:
                break
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                line = line[:index]
                break
            index += 1
        lines.append(line)
    return "".join(lines)


def resolve_tex_path(base: Path, value: str) -> Path:
    path = (base / value).resolve()
    if path.suffix == "":
        path = path.with_suffix(".tex")
    return path


def expand_inputs(source: str, base: Path, stack: tuple[Path, ...] = ()) -> str:
    def replace(match: re.Match[str]) -> str:
        path = resolve_tex_path(base, match.group(1).strip())
        if path in stack:
            chain = " -> ".join(str(item) for item in (*stack, path))
            raise ValueError(f"cyclic LaTeX input: {chain}")
        if not path.is_file():
            raise FileNotFoundError(f"LaTeX input not found: {path}")
        nested = path.read_text(encoding="utf-8")
        return expand_inputs(nested, path.parent, (*stack, path))

    return INPUT_PATTERN.sub(replace, source)


def extract_body(main_source: str) -> str:
    start = BODY_START_PATTERN.search(main_source)
    if not start:
        raise ValueError("body start command \\pesudohookOFpremainbody not found")
    end = BODY_END_PATTERN.search(main_source, start.end())
    if not end:
        raise ValueError("body end input \\input{references} not found")
    body = main_source[start.end() : end.start()]
    return re.sub(r"\\clearpage\s*$", "", body)


def skip_space(source: str, index: int) -> int:
    while index < len(source) and source[index].isspace():
        index += 1
    return index


def parse_group(source: str, index: int, opening: str, closing: str) -> tuple[str, int]:
    index = skip_space(source, index)
    if index >= len(source) or source[index] != opening:
        return "", index
    depth = 1
    cursor = index + 1
    start = cursor
    while cursor < len(source):
        char = source[cursor]
        if char == "\\":
            cursor += 2
            continue
        if char == opening:
            depth += 1
        elif char == closing:
            depth -= 1
            if depth == 0:
                return source[start:cursor], cursor + 1
        cursor += 1
    raise ValueError(f"unclosed {opening}{closing} group")


def strip_latex(source: str) -> str:
    source = remove_comments(source)
    output: list[str] = []
    index = 0

    while index < len(source):
        char = source[index]

        if char == "$":
            delimiter = "$$" if source.startswith("$$", index) else "$"
            end = source.find(delimiter, index + len(delimiter))
            if end < 0:
                raise ValueError(f"unclosed math delimiter {delimiter}")
            index = end + len(delimiter)
            continue

        if char in "{}~&":
            output.append(" " if char == "~" else "")
            index += 1
            continue

        if char != "\\":
            output.append(char)
            index += 1
            continue

        if index + 1 >= len(source):
            index += 1
            continue

        next_char = source[index + 1]
        if next_char in ESCAPED_CHARACTERS:
            output.append(next_char)
            index += 2
            continue
        if next_char in ",;:! \\":
            output.append(" ")
            index += 2
            continue
        if next_char in "([":
            closing = ")" if next_char == "(" else "]"
            delimiter = "\\" + closing
            end = source.find(delimiter, index + 2)
            if end < 0:
                raise ValueError(f"unclosed math delimiter \\{next_char}")
            index = end + 2
            continue

        match = re.match(r"\\([A-Za-z@]+)\*?", source[index:])
        if not match:
            index += 2
            continue
        command = match.group(1)
        index += match.end()

        while True:
            optional_start = skip_space(source, index)
            if optional_start >= len(source) or source[optional_start] != "[":
                break
            _, index = parse_group(source, optional_start, "[", "]")

        if command == "begin":
            environment, index = parse_group(source, index, "{", "}")
            optional_start = skip_space(source, index)
            if optional_start < len(source) and source[optional_start] == "[":
                _, index = parse_group(source, optional_start, "[", "]")
            if environment in VERBATIM_ENVIRONMENTS:
                if environment == "minted":
                    _, index = parse_group(source, index, "{", "}")
                delimiter = f"\\end{{{environment}}}"
                end = source.find(delimiter, index)
                if end < 0:
                    raise ValueError(f"unclosed environment {environment}")
                output.append(source[index:end])
                index = end + len(delimiter)
            else:
                for _ in range(ENVIRONMENT_ARGUMENTS.get(environment, 0)):
                    _, index = parse_group(source, index, "{", "}")
            continue
        if command == "end":
            _, index = parse_group(source, index, "{", "}")
            continue
        if command == "verb":
            index = skip_space(source, index)
            if index >= len(source):
                raise ValueError("missing \\verb delimiter")
            delimiter = source[index]
            end = source.find(delimiter, index + 1)
            if end < 0:
                raise ValueError("unclosed \\verb content")
            output.append(source[index + 1 : end])
            index = end + 1
            continue
        if command == "href":
            _, index = parse_group(source, index, "{", "}")
            continue
        if command in DISCARD_ARGUMENTS:
            for _ in range(DISCARD_ARGUMENTS[command]):
                _, index = parse_group(source, index, "{", "}")
            continue
        if command in VISIBLE_COMMANDS:
            output.append(VISIBLE_COMMANDS[command])

    text = "".join(output)
    return text.replace("---", "—").replace("--", "–").replace("``", "“").replace("''", "”")


def is_chinese(char: str) -> bool:
    codepoint = ord(char)
    return (
        0x3400 <= codepoint <= 0x4DBF
        or 0x4E00 <= codepoint <= 0x9FFF
        or 0xF900 <= codepoint <= 0xFAFF
        or 0x20000 <= codepoint <= 0x323AF
    )


def count_text(text: str) -> Counts:
    chinese = sum(is_chinese(char) for char in text)
    english = sum(("A" <= char <= "Z") or ("a" <= char <= "z") for char in text)
    punctuation = sum(unicodedata.category(char).startswith("P") for char in text)
    return Counts(chinese, english, punctuation)


def load_section(path: Path) -> str:
    source = path.read_text(encoding="utf-8")
    return expand_inputs(source, path.parent, (path.resolve(),))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Count Chinese Han characters, English letters, and Unicode punctuation "
            "in abstract, body, references, and appendices while removing LaTeX syntax."
        )
    )
    parser.add_argument("-m", "--main", type=Path, default=Path("main.tex"))
    parser.add_argument("-a", "--abstract", type=Path, default=Path("abstract.tex"))
    parser.add_argument("-r", "--references", type=Path, default=Path("references.tex"))
    parser.add_argument("-A", "--appendices", type=Path, default=Path("appendices.tex"))
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        help="show selected files and body boundaries without reading/counting content",
    )
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args()
    paths = {
        "abstract": args.abstract.resolve(),
        "body": args.main.resolve(),
        "references": args.references.resolve(),
        "appendices": args.appendices.resolve(),
    }

    if args.dry_run:
        print("Read-only plan:")
        for name, path in paths.items():
            detail = " (between \\pesudohookOFpremainbody and \\input{references})" if name == "body" else ""
            print(f"  {name}: {path}{detail}")
        print("No files read; no files changed.")
        return 0

    try:
        main_source = args.main.read_text(encoding="utf-8")
        sections = {
            "abstract": load_section(args.abstract),
            "body": expand_inputs(extract_body(main_source), args.main.parent, (args.main.resolve(),)),
            "references": load_section(args.references),
            "appendices": load_section(args.appendices),
        }
        counts = {name: count_text(strip_latex(source)) for name, source in sections.items()}
    except (FileNotFoundError, OSError, UnicodeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"{'section':<12} {'Chinese':>8} {'English':>8} {'punctuation':>12} {'total':>8}")
    print("-" * 52)
    grand_total = Counts()
    for name, section_counts in counts.items():
        grand_total += section_counts
        print(
            f"{name:<12} {section_counts.chinese:>8} {section_counts.english:>8} "
            f"{section_counts.punctuation:>12} {section_counts.total:>8}"
        )
    print("-" * 52)
    print(
        f"{'total':<12} {grand_total.chinese:>8} {grand_total.english:>8} "
        f"{grand_total.punctuation:>12} {grand_total.total:>8}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

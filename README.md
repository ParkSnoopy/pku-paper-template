# Unofficial Course Paper Template

A self-contained, unofficial XeLaTeX template for an undergraduate humanities course paper. The sample document uses neutral Lorem Ipsum text and placeholder metadata so it can be reused without retaining content from a specific paper.

> [!WARNING]
> **Fonts are not bundled.** The following fonts must be installed on your system before compiling:
>
> - **Times New Roman** — for Latin text
> - **SimSun** (宋体) — for Chinese body text
> - **SimHei** (黑体) — for Chinese headings and bold
> - **KaiTi** (楷体) — for the author name on the cover
>
> These are proprietary system fonts (Microsoft / ZYEC). They are not redistributable, so they are excluded from this repository. The class loads them by font name; install them via your OS package manager or place them in your system's font directory.

## Files

- `main.tex`: document metadata, example structure, and sample text
- `main.cls`: document class and cover/body formatting
- `abstract.tex`: the single Chinese abstract and keywords
- `references.tex`: example bibliography entries
- `appendices.tex`: figure, table, and code-block examples
- `tools/count_content.py`: content-only character counter
- `tools/tests/`: standard-library tests for the character counter
- `figures/`: local images used by the document examples
- `logo.png`: cover logo
- `fonts/`: optional local override for system fonts (not tracked)
- `latexmkrc`: XeLaTeX build configuration

## Customize

1. Replace the metadata values near the top of `main.tex`.
   The example title scopes its English text with `{\rmfamily ...}` so it uses the bundled Times New Roman font while the surrounding Chinese title keeps the configured CJK title font.
2. Replace the Chinese abstract and keywords in `abstract.tex`.
3. Replace the Lorem Ipsum paragraphs and example section titles in `main.tex`.
4. Replace the sample entries in `references.tex` and update the corresponding citation keys.
5. Replace or remove the demonstrations in `appendices.tex` as needed.
6. Keep `\documentclass[BAhumanities,customization]{main}` unless you intentionally change the document mode or font setup.

## Build

Run:

```sh
latexmk main.tex
```

Clean generated intermediate files with:

```sh
latexmk -c
```

The final PDF is written to `main.pdf`.

## Count content characters

Run:

```sh
python3 tools/count_content.py
```

The script reports separate and combined counts for the abstract, body, references, and appendices. The body is the part of `main.tex` between `\pesudohookOFpremainbody` and `\input{references}`; nested `\input` and `\include` files within that range are expanded recursively.

The total includes Chinese Han characters, ASCII English letters, and Unicode punctuation. It excludes whitespace, digits, emoji, comments, math, LaTeX commands, citation and reference keys, labels, environment options, and layout arguments. Visible headings, captions, keywords, URLs, inline verbatim text, and code listings remain content and are counted.

Preview selected files and boundaries without reading content:

```sh
python3 tools/count_content.py --dry-run
```

Override default paths with `-m`/`--main`, `-a`/`--abstract`, `-r`/`--references`, and `-A`/`--appendices`. Use `-n` as the short form of `--dry-run`.

## Attribution

**Origin base:** [dlmuthesis LaTeX Thesis Template for Dalian Maritime University](https://www.overleaf.com/latex/templates/dlmuthesis-latex-thesis-template-for-dalian-maritime-university/rmstrjjrthwf)

The class retains the LPPL-licensed DLMU thesis class as its typographic base and adds an unofficial course-paper cover adaptation. The provided origin archive was used to verify the Chinese abstract, table-of-contents, bibliography, appendix, figure, table, and code-block workflows. See the license header in `main.cls`.

## License

This project is licensed under the **GNU General Public License v3.0 or later** (`GPL-3.0-or-later`).

The GPL is a copyleft license: derivative works must be distributed under the same license terms, and their source code must be made available.

# Project Context

## Purpose

This repository is a reusable, unofficial XeLaTeX template for an undergraduate humanities course paper. It contains only neutral example content and editable placeholder metadata.

The sample metadata intentionally formats the course name as `《课程名称》课程论文`, keeps the date in Chinese numerals, and includes scoped English title text to demonstrate mixed CJK and Times New Roman typography. The document contains one Chinese abstract, a table of contents, neutral Chinese and Lorem Ipsum body examples, three consecutively numbered second-level sections, a dedicated references page, and appendices demonstrating an origin-derived figure, table, and code block.

The cover intentionally keeps only the `姓名`, `学号`, and `院系` information rows. Flush-left headings and balanced undergraduate page geometry are also intentional local adaptations and must not be reverted to the origin class defaults.

Heading numbering follows `一、` for sections, then decimal subsections (`1.1`, `1.2`, `2.4`), subsubsections (`1.2.1`, `2.4.2`), and paragraphs (`1.2.1.1`). Parentheses and Chinese numerals are not used for these lower levels.

## Source layout

- `main.tex` is the user-facing entry point.
- `main.cls` owns reusable layout, typography, cover rendering, and citation commands.
- `abstract.tex` contains the only abstract, in Chinese.
- `references.tex` contains replaceable example bibliography entries.
- `appendices.tex` contains replaceable figure, table, and code examples.
- `tools/count_content.py` means the repository's content-length counter: it counts Chinese Han characters, ASCII English letters, and Unicode punctuation in the abstract, body, references, and appendices after removing non-content LaTeX syntax.
- `tools/tests/` contains standard-library regression tests for content extraction and counting.
- `logo.png` and `figures/` are local runtime assets.
- `latexmkrc` configures the reproducible XeLaTeX build.
- `.gitignore` excludes generated LaTeX intermediates and the reproducible `main.pdf` output.
- `fonts/` is excluded from version control because fonts are loaded by name from the system, not bundled.
- `LICENSE` contains the full GPL-3.0 text.

## Build contract

Run `latexmk main.tex` from the repository root. The document class, abstract, bibliography, appendices, images, logo, and bundled fonts must resolve locally; the template must not depend on the origin archive or extracted review directories.

## Editing boundaries

Keep paper content and metadata in `main.tex`, abstract content in `abstract.tex`, bibliography data in `references.tex`, appendix examples in `appendices.tex`, and reusable formatting in `main.cls`. Preserve the upstream license header when modifying the class.

“Content length” excludes whitespace, digits, emoji, comments, math, commands, citation/reference keys, labels, and layout arguments. Visible titles, headings, captions, keywords, URLs, inline verbatim text, and code listings remain content. The body boundary starts after `\pesudohookOFpremainbody` and ends before `\input{references}`; nested body inputs are content.

Counter path overrides use `-m`/`--main`, `-a`/`--abstract`, `-r`/`--references`, and `-A`/`--appendices`; dry-run uses `-n`/`--dry-run`.

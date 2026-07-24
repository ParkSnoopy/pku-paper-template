# Project Context

## Purpose

This repository is a reusable, unofficial XeLaTeX template for an undergraduate humanities course paper. It contains only neutral example content and editable placeholder metadata.

The sample metadata intentionally formats the course name as `《课程名称》课程论文`, keeps the date in Chinese numerals, and includes scoped English title text to demonstrate mixed CJK and Times New Roman typography. The body includes both neutral Chinese copy and Lorem Ipsum examples.

## Source layout

- `main.tex` is the user-facing entry point.
- `main.cls` owns reusable layout, typography, cover rendering, and citation commands.
- `refs.tex` contains replaceable example bibliography entries.
- `logo.png` and `fonts/` are local runtime assets.
- `latexmkrc` configures the reproducible XeLaTeX build.
- `.gitignore` excludes generated LaTeX intermediates and the reproducible `main.pdf` output.

## Build contract

Run `latexmk main.tex` from the repository root. The document class, bibliography input, logo, and bundled fonts must resolve locally; the template must not depend on removed reference directories or topic-specific source files.

## Editing boundaries

Keep paper content and metadata in `main.tex`, bibliography data in `refs.tex`, and reusable formatting in `main.cls`. Preserve the upstream license header when modifying the class.

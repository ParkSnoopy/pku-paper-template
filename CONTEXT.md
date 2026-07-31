# Paper Template — Project Context

## Purpose

This repository contains reusable, unofficial XeLaTeX course-paper templates under `templates/`. Each template keeps neutral example content and editable metadata separate from reusable formatting.

Current templates:

- `templates/dlmuthesis`: undergraduate humanities course paper derived from the LPPL-licensed DLMU thesis class.
- `templates/zhuangzizhexue`: philosophy course paper reconstructed from course format requirements and a verified submission. Source artifacts were removed after extraction; the extracted rules are documented in the template's README and class.

Neither template is an official institution-published LaTeX package.

## Shared conventions

- `main.tex` is each template's user-facing entry point.
- `main.cls` owns reusable layout and typography.
- `latexmkrc` configures XeLaTeX builds.
- Fonts are loaded by installed system name and are not bundled.
- Generated `main.pdf` files and LaTeX intermediates stay untracked.
- Keep user examples neutral. When a template is reconstructed from supplied source documents, extract all rules into the template class and README, then remove the source artifacts.
- Use no more than year precision for project history and class metadata. Keep exact dates only where technically required.

## `dlmuthesis`

This template contains one Chinese abstract, a table of contents, neutral Chinese and Lorem Ipsum body examples, a dedicated references page, and appendices demonstrating figures, tables, and code.

Intentional adaptations:

- Cover contains only `姓名`, `学号`, and `院系` information rows.
- Headings are flush left.
- Undergraduate page geometry is balanced.
- Sections use `一、`; lower levels use decimal numbering (`1.1`, `1.1.1`, `1.1.1.1`).

Additional files:

- `abstract.tex`: Chinese abstract.
- `references.tex`: replaceable bibliography entries.
- `appendices.tex`: replaceable figure, table, and code examples.
- `tools/count_content.py`: content-length counter.
- `tools/tests/`: counter regression tests.
- `logo.png` and `figures/`: local runtime assets.

Content counting includes Chinese Han characters, ASCII English letters, and Unicode punctuation. It excludes whitespace, digits, emoji, comments, math, commands, citation/reference keys, labels, and layout arguments. Visible headings, captions, keywords, URLs, inline verbatim text, and code listings remain content.

## `zhuangzizhexue`

Formatting was reconstructed from the course format requirements and a verified submitted paper; source artifacts were removed after extraction. Extracted rules:

1. Body: five-size font (10.5 bp), SimSun Chinese, Times New Roman Western, 1.5 line spacing, two-character first-line indent.
2. Citations: footnotes only, no end-of-paper bibliography; seven source-type patterns (Chinese monograph, translation, thesis, journal, collected journal, foreign monograph, foreign journal) are documented with examples in the template README.
3. Structure: for ~3,000-character papers, at most three numbered body sections excluding 引言 and 结语.
4. Title block: centered SimHei title (16 bp) and subtitle (14 bp), KaiTi author name, affiliation and student ID in a serif fallback, all on the first body page (no separate cover).
5. Page geometry: A4, 2.5 cm top/bottom, 1.75 cm left/right margins; centered course-title header with rule; centered Arabic page-number footer.
6. Headings: centered 14 bp bold SimHei; numbered sections render as `一、`, `二、`, `三、`.
7. Footnotes: 9 bp text, 25%-width separator rule, circled numbers (①②③…) restarting each page.

When evidence differs, explicit course-format instructions win. The exported submission visually omits some required first-line indents; the LaTeX class enforces the explicit two-character requirement.

Reconstructed invariants:

- A4, 2.5 cm top/bottom and 1.75 cm left/right margins.
- Body is 10.5 bp SimSun/Times New Roman with a 15.6 bp baseline and two-character first-line indent.
- Title is centered 16 bp bold SimHei; subtitle and headings are centered 14 bp bold SimHei.
- Author uses KaiTi. Affiliation uses SimSun as a portable fallback for the source PDF's FangSong.
- Header contains centered course title and a rule. Footer contains centered Arabic page number.
- Numbered sections render as `一、`, `二、`, `三、`; introduction and conclusion use unnumbered sections.
- Citations use real footnotes. Circled footnote numbers restart each page; no separate bibliography is generated.

## Build contract

Build from each template directory:

```sh
cd templates/dlmuthesis && latexmk main.tex
cd templates/zhuangzizhexue && latexmk main.tex
```

A clean build must resolve local classes, inputs, and assets without depending on extracted temporary directories. Font prerequisites must be installed by system name.

## Editing boundaries

Keep content and metadata in each `main.tex`; keep reusable formatting in its `main.cls`. For `dlmuthesis`, preserve separate abstract, references, appendices, counter tools, and upstream license header. For `zhuangzizhexue`, keep the extracted format rules in the class and README since source artifacts were removed.

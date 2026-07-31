# Changelog

## 2026

### Add

- Add `templates/zhuangzizhexue` as a reusable, unofficial XeLaTeX course-paper template reconstructed from course format requirements and a verified submission.
- Add source-grounded A4 geometry, title metadata, centered SimHei headings, installed-font checks, repeated course header, page footer, and per-page circled footnotes.
- Add neutral examples for the required footnote-only citation workflow and document all seven supplied citation orders.
- Add a dependency-free script under `tools/` that counts Chinese, English, and punctuation characters across the abstract, body, references, and appendices while excluding LaTeX syntax.
- Add focused tests under `tools/tests/` for syntax removal, body extraction, recursive inputs, environment arguments, verbatim content, and character classification.
- Add short command-line aliases for every content-counter option.
- Add template usage and project-structure documentation.
- Add LaTeX build-artifact ignore rules.
- Add a neutral Chinese body-text example.
- Add examples for three consecutively numbered second-level sections.
- Add one Chinese abstract and a table of contents following the origin humanities workflow.
- Add appendices with origin-derived figure, table, and code-block examples.
- Switch lower-level headings to decimal numbering: `1.1`, `1.1.1`, and `1.1.1.1`.
- Add origin-base reference link and font-license documentation.
- Adopt GPL-3.0-or-later as the project license.
- Load fonts by system font name instead of bundled file paths.

### Update

- Reframe repository context and build instructions around multiple templates under `templates/`.
- Prefer explicit course-format requirements over inconsistent submission rendering, including mandatory two-character first-line indentation.
- Remove day-level dates from project history and class metadata while retaining exact dates required for dependency-version checks.
- Replace paper-specific content with neutral placeholders and Lorem Ipsum examples.
- Keep the example date in Chinese numerals.
- Demonstrate Times New Roman in the English portion of the title.
- Format the example course name with Chinese book-title marks.
- Start the example references on a dedicated page.
- Rename `refs.tex` to `references.tex` and update all imports.
- Remove direct university naming and clarify the template's unofficial status.

### Fix

- Align class, bibliography, and logo imports with the repository filenames.
- Verify the class against the origin bundle while preserving intentional heading, geometry, and cover-field adaptations.

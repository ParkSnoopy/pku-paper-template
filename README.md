# Unofficial Course Paper Template

A self-contained, unofficial XeLaTeX template for an undergraduate humanities course paper. The sample document uses neutral Lorem Ipsum text and placeholder metadata so it can be reused without retaining content from a specific paper.

## Files

- `main.tex`: document metadata, example structure, and sample text
- `main.cls`: document class and cover/body formatting
- `refs.tex`: example bibliography entries
- `logo.png`: cover logo
- `fonts/`: bundled fonts required by `customization` mode
- `latexmkrc`: XeLaTeX build configuration

## Customize

1. Replace the metadata values near the top of `main.tex`.
   The example title scopes its English text with `{\rmfamily ...}` so it uses the bundled Times New Roman font while the surrounding Chinese title keeps the configured CJK title font.
2. Replace the Lorem Ipsum paragraphs and example section titles.
3. Replace the sample entries in `refs.tex` and update the corresponding citation keys.
4. Keep `\documentclass[BAhumanities,customization]{main}` unless you intentionally change the document mode or font setup.

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

## Attribution

The class retains the LPPL-licensed DLMU thesis class as its typographic base and adds an unofficial course-paper cover adaptation. See the license header in `main.cls`.

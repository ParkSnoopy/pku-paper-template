# Unofficial Course Paper Template

A self-contained, unofficial XeLaTeX template for an undergraduate humanities course paper. The sample document uses neutral Lorem Ipsum text and placeholder metadata so it can be reused without retaining content from a specific paper.

## Files

- `main.tex`: document metadata, example structure, and sample text
- `main.cls`: document class and cover/body formatting
- `abstract.tex`: the single Chinese abstract and keywords
- `references.tex`: example bibliography entries
- `appendices.tex`: figure, table, and code-block examples
- `figures/`: local images used by the document examples
- `logo.png`: cover logo
- `fonts/`: bundled fonts required by `customization` mode
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

## Attribution

The class retains the LPPL-licensed DLMU thesis class as its typographic base and adds an unofficial course-paper cover adaptation. The provided origin archive was used to verify the Chinese abstract, table-of-contents, bibliography, appendix, figure, table, and code-block workflows. See the license header in `main.cls`.

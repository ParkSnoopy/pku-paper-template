# Paper Template

Reusable, unofficial XeLaTeX course-paper templates. Each template keeps neutral example content and editable metadata separate from reusable formatting, so you can drop in your own paper without touching layout code.

## Templates

| Template | Use case | Key features |
|----------|----------|--------------|
| `templates/dlmuthesis` | Undergraduate humanities course paper (DLMU-derived) | Chinese abstract, TOC, bibliography, appendices, cover page |
| `templates/zhuangzizhexue` | Philosophy course paper | Footnote-only citations, circled per-page footnotes, compact title block |

## Quick start

Pick a template, edit `main.tex` metadata, then build:

```sh
cd templates/<name>
latexmk main.tex
```

Output: `main.pdf` in the same directory.

## Fonts

> [!WARNING]
> **Fonts are not bundled.** The following fonts must be installed on your system before compiling:
>
> - **Times New Roman** — for Latin text
> - **SimSun** (宋体) — for Chinese body text
> - **SimHei** (黑体) — for Chinese headings and bold
> - **KaiTi** (楷体) — for the author name on the cover
>
> These are proprietary system fonts (Microsoft / ZYEC). They are not redistributable, so they are excluded from this repository. The class loads them by font name; install them via your OS package manager or place them in your system's font directory.

## Documentation

- `CONTEXT.md` — design decisions, invariants, editing boundaries
- `CHANGELOG.md` — project history
- Each template has its own `README.md` with format details and citation rules

## License

GPL-3.0-or-later. See template READMEs for origin attributions.

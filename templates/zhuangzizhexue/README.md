# Paper Template

Self-contained XeLaTeX template for a philosophy course paper. Reconstructed from course format requirements and verified against a rendered submission; source artifacts have been removed after extraction. Follows the reusable class/entry-point split used by the sibling `dlmuthesis` template.

## Files

- `main.tex`: user-facing metadata and neutral examples.
- `main.cls`: reusable A4 layout, fonts, title block, headings, header/footer, and footnotes.
- `latexmkrc`: deterministic XeLaTeX build configuration.

No image assets are required by this template.

## Customize

Edit metadata near the top of `main.tex`:

```tex
\coursetitle{《课程名称》课程论文}
\cntitle{主标题}
\papersubtitle{——副标题}
\aauthor{姓名}
\faculty{XX院校，XX系}
\stuid{学号}
```

Use numbered `\section{...}` commands for the suggested maximum of three body sections. Use `\section*{引言}` and `\section*{结语}` for unnumbered opening and closing sections.

All source citations belong in real `\footnote{...}` commands. Circled footnote numbers restart on each page. Do not replace notes with parenthetical plain text or a separate bibliography unless course requirements change.

## Footnote citation order

Follow the course format for each source type:

1. Chinese monograph: author/responsibility, title, optional volume, publisher, year, page.
   示例：冯友兰：《新理学》，《三松堂全集》第四卷，河南人民出版社，2001年，第5页。
2. Translation: author/responsibility, title, optional volume, translator, publisher, year, page.
   示例：马克斯·韦伯：《儒教与道教》，王容芬译，江苏人民出版社，2002年，第1页。
3. Thesis: author, thesis title, degree-granting institution and degree, defense year, page.
   示例：刘笑敢：《庄子哲学的体系及庄学的演变》，北京大学博士学位论文，1985年，第42页。
4. Journal article: author, article title, journal, year/issue or volume/issue.
   示例：陈来：《中国哲学史的学科属性与方法》，《中国哲学史》2021年第4期。
5. Collected journal: author, article title, collection, volume/issue, publisher, year, page.
   示例：梁漱溟：《自述早年思想之再转再变》，《中国哲学》第1辑，生活·读书·新知三联书店，1979年，第336页。
6. Foreign monograph: author/responsibility, title, city, publisher, year, page.
   示例：Benjamin I. Schwartz, *The World of Thought in Ancient China*, Cambridge: Belknap Press of Harvard University Press, 1985, pp.25-27.
7. Foreign journal article: author, article title, journal, volume/issue, year, page.
   示例：Roger T. Ames, "On How to Construct a Confucian Democracy for Modern Times", *Philosophy East & West*, Vol. 67, No. 1, 2017, pp. 61-81.

## Build

From this directory:

```sh
latexmk main.tex
```

Final file: `main.pdf`.

Clean intermediates:

```sh
latexmk -c
```

## Reconstructed format

- A4 paper.
- Margins: 2.5 cm top/bottom, 1.75 cm left/right.
- Body: five-size (10.5 bp), SimSun Chinese, Times New Roman Western text, 15.6 bp baseline, two-character first-line indent.
- Title: centered 16 bp bold SimHei.
- Subtitle and headings: centered 14 bp bold SimHei.
- Author: centered KaiTi; affiliation/student ID: centered SimSun (source used FangSong).
- Header: centered course title, 9 bp, with rule.
- Footer: centered Arabic page number, 9 bp.
- Footnotes: 9 bp, 25%-width separator, circled numbers restarting each page.
- Structure advice: for ~3,000-character papers, use at most three numbered body sections (excluding 引言 and 结语).

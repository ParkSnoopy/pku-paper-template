% Unofficial course-paper class reconstructed from course format requirements
% and a verified submission. Source artifacts were removed after extraction.
% !TeX program = xelatex
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{main}

\RequirePackage{iftex}
\ifXeTeX\else
  \ClassError{main}{XeLaTeX is required}{Compile with xelatex or latexmk.}
\fi

\LoadClass[UTF8,scheme=plain,fontset=none,zihao=5,a4paper]{ctexart}

\RequirePackage{fontspec}
\RequirePackage{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{perpage}
\RequirePackage{xparse}
\RequirePackage{xurl}
\RequirePackage[hidelinks,unicode]{hyperref}

% Source page: A4; 2.5 cm vertical and 1.75 cm horizontal margins.
\geometry{
  top=2.5cm,
  bottom=2.5cm,
  left=1.75cm,
  right=1.75cm,
  headheight=12bp,
  headsep=16.3bp,
  footskip=21.25bp
}

% Supplied fonts are proprietary system fonts and are intentionally not bundled.
\IfFontExistsTF{Times New Roman}{
  \setmainfont{Times New Roman}[
    BoldFont=Times New Roman,
    ItalicFont=Times New Roman,
    BoldItalicFont=Times New Roman
  ]
}{
  \ClassError{main}{Times New Roman is not installed}{Install Times New Roman before compiling.}
}
\IfFontExistsTF{SimSun}{
  \setCJKmainfont{SimSun}[AutoFakeBold=3]
  \setCJKmonofont{SimSun}
  \newCJKfontfamily\coursepapersong{SimSun}[AutoFakeBold=3]
  \newfontfamily\coursepapercircledfont{SimSun}
}{
  \ClassError{main}{SimSun is not installed}{Install SimSun before compiling.}
}
\IfFontExistsTF{SimHei}{
  \setCJKsansfont{SimHei}[AutoFakeBold=3]
  \newCJKfontfamily\coursepaperhei{SimHei}[AutoFakeBold=3]
}{
  \ClassError{main}{SimHei is not installed}{Install SimHei before compiling.}
}
\IfFontExistsTF{KaiTi}{
  \newCJKfontfamily\paperauthorfont{KaiTi}
}{
  \ClassError{main}{KaiTi is not installed}{Install KaiTi before compiling.}
}
% Supplied PDF uses FangSong for affiliation. SimSun fallback avoids
% non-portable FangSong family names while preserving serif appearance.
\newcommand{\paperaffiliationfont}{\coursepapersong}

\setlength{\parindent}{2em}
\setlength{\parskip}{0bp}
\AtBeginDocument{\fontsize{10.5bp}{15.6bp}\selectfont}
\urlstyle{same}

% User-facing metadata, aligned with sibling dlmuthesis template.
\newcommand{\coursepapertitle}{《课程名称》课程论文}
\newcommand{\coursepapermain}{主标题}
\newcommand{\coursepapersubtitle}{——副标题}
\newcommand{\coursepaperauthor}{姓名}
\newcommand{\coursepaperfaculty}{XX院校，XX系}
\newcommand{\coursepaperstudentid}{学号}
\newcommand{\coursetitle}[1]{\renewcommand{\coursepapertitle}{#1}}
\newcommand{\cntitle}[1]{\renewcommand{\coursepapermain}{#1}}
\newcommand{\papersubtitle}[1]{\renewcommand{\coursepapersubtitle}{#1}}
\newcommand{\aauthor}[1]{\renewcommand{\coursepaperauthor}{#1}}
\newcommand{\faculty}[1]{\renewcommand{\coursepaperfaculty}{#1}}
\newcommand{\stuid}[1]{\renewcommand{\coursepaperstudentid}{#1}}

% Header and footer reproduced from exported PDF.
\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{\coursepapersong\fontsize{9bp}{12bp}\selectfont\coursepapertitle}
\fancyfoot[C]{\rmfamily\fontsize{9bp}{12bp}\selectfont\thepage}
\renewcommand{\headrulewidth}{0.5bp}
\renewcommand{\footrulewidth}{0bp}
\fancypagestyle{plain}{
  \fancyhf{}
  \fancyhead[C]{\coursepapersong\fontsize{9bp}{12bp}\selectfont\coursepapertitle}
  \fancyfoot[C]{\rmfamily\fontsize{9bp}{12bp}\selectfont\thepage}
  \renewcommand{\headrulewidth}{0.5bp}
  \renewcommand{\footrulewidth}{0bp}
}

% Centered 14 bp SimHei headings. Numbered sections use 一、二、三、….
\ctexset{
  section = {
    format = \centering\coursepaperhei\bfseries\fontsize{14bp}{15.6bp}\selectfont,
    name = {,、},
    number = \chinese{section},
    aftername = {},
    beforeskip = 15.6bp,
    afterskip = 15.6bp
  }
}
\setcounter{secnumdepth}{1}

% Title block remains on first body page, not a separate cover.
\newcommand{\makepages}{%
  \thispagestyle{fancy}%
  \begin{center}
    {\coursepaperhei\bfseries\fontsize{16bp}{24bp}\selectfont\coursepapermain\par}
    \vspace{25.6bp}%
    {\coursepaperhei\bfseries\fontsize{14bp}{21bp}\selectfont\coursepapersubtitle\par}
    \vspace{50.2bp}%
    {\paperauthorfont\fontsize{10.5bp}{15.6bp}\selectfont\coursepaperauthor\par}
    \vspace{7.8bp}%
    {\paperaffiliationfont\fontsize{10.5bp}{15.6bp}\selectfont
      （\coursepaperfaculty，\coursepaperstudentid）\par}
  \end{center}
  \vspace{31.2bp}%
}

% Circled footnote numbers restart on each page, matching supplied documents.
\MakePerPage{footnote}
\newcommand{\coursepapercircled}[1]{%
  \ifcase#1\or ①\or ②\or ③\or ④\or ⑤\or ⑥\or ⑦\or ⑧\or ⑨\or ⑩%
  \or ⑪\or ⑫\or ⑬\or ⑭\or ⑮\or ⑯\or ⑰\or ⑱\or ⑲\or ⑳%
  \else\textcircled{\scriptsize#1}\fi}
\renewcommand{\thefootnote}{\coursepapercircled{\value{footnote}}}
\makeatletter
\renewcommand{\@makefnmark}{%
  \hbox{\textsuperscript{\normalfont\coursepapercircledfont\@thefnmark}}}
\makeatother
\renewcommand{\footnoterule}{%
  \kern-3bp
  \hrule width .25\textwidth height .5bp
  \kern2.86bp
}
\setlength{\skip\footins}{12bp plus 2bp minus 2bp}
\setlength{\footnotesep}{10.8bp}
\renewcommand{\footnotesize}{\fontsize{9bp}{10.8bp}\selectfont}

\AtBeginDocument{%
  \hypersetup{
    pdftitle={\coursepapermain},
    pdfauthor={\coursepaperauthor}
  }%
}

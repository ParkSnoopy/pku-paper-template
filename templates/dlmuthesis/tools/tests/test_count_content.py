import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).parents[1] / "count_content.py"
SPEC = importlib.util.spec_from_file_location("count_content", SCRIPT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {SCRIPT_PATH}")
count_content = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = count_content
SPEC.loader.exec_module(count_content)


class ContentCounterTests(unittest.TestCase):
    def test_short_arguments(self):
        args = count_content.parse_args(
            ["-m", "paper.tex", "-a", "summary.tex", "-r", "sources.tex", "-A", "extras.tex", "-n"]
        )

        self.assertEqual(args.main, Path("paper.tex"))
        self.assertEqual(args.abstract, Path("summary.tex"))
        self.assertEqual(args.references, Path("sources.tex"))
        self.assertEqual(args.appendices, Path("extras.tex"))
        self.assertTrue(args.dry_run)

    def test_strips_latex_syntax_but_keeps_visible_text(self):
        source = r"""
        % hidden comment
        \section{标题 Title}
        正文，\textbf{bold}! \upcite{source-key}
        \href{https://hidden.example}{Link} \url{https://shown.example/a-b}
        $x+y$ \(z\) escaped \% and en--dash.
        """
        text = count_content.strip_latex(source)

        self.assertNotIn("hidden comment", text)
        self.assertNotIn("source-key", text)
        self.assertNotIn("hidden.example", text)
        self.assertNotIn("x+y", text)
        self.assertIn("标题 Title", text)
        self.assertIn("正文，bold!", text)
        self.assertIn("Link", text)
        self.assertIn("https://shown.example/a-b", text)
        self.assertIn("escaped % and en–dash.", text)

    def test_verbatim_content_excludes_environment_options(self):
        source = r"""\begin{lstlisting}[language=C++]
int main() { return 0; }
\end{lstlisting}"""
        text = count_content.strip_latex(source)

        self.assertNotIn("language", text)
        self.assertIn("int main() { return 0; }", text)

    def test_environment_layout_arguments_are_not_content(self):
        source = r"""\begin{figure}[H]
\begin{tabular}{cccc}
Visible & Text \\
\end{tabular}
\end{figure}"""
        text = count_content.strip_latex(source)

        self.assertNotIn("H", text)
        self.assertNotIn("cccc", text)
        self.assertNotIn("&", text)
        self.assertIn("Visible", text)
        self.assertIn("Text", text)

    def test_inline_verbatim_keeps_code_without_delimiters(self):
        text = count_content.strip_latex(r"Use \verb|x_y()| now.")

        self.assertIn("x_y()", text)
        self.assertNotIn("|", text)

    def test_counts_only_requested_character_classes(self):
        counts = count_content.count_text("中文 Ab!，123🙂")

        self.assertEqual(counts, count_content.Counts(chinese=2, english=2, punctuation=2))
        self.assertEqual(counts.total, 6)

    def test_extracts_body_and_expands_nested_inputs(self):
        with tempfile.TemporaryDirectory(prefix="hermes-verify-content-counter-") as directory:
            root = Path(directory)
            (root / "part.tex").write_text("嵌套 body.", encoding="utf-8")
            main_source = r"""
\input{abstract}
\pesudohookOFpremainbody
正文 \input{part}
\clearpage
\input{references}
\input{appendices}
"""
            body = count_content.extract_body(main_source)
            expanded = count_content.expand_inputs(body, root)

        self.assertIn("正文", expanded)
        self.assertIn("嵌套 body.", expanded)
        self.assertNotIn("references", expanded)
        self.assertNotIn("appendices", expanded)


if __name__ == "__main__":
    unittest.main()

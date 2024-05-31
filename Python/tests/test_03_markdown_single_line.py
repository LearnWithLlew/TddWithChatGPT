from textwrap import dedent

from tests.line import Line
from tests.markdown_printer import MarkdownPrinter


def test_create_markdown():
   expected_markdown = dedent("""
   <pre style="color: gray">
   one <b style="color: red">too </b>three.
   </pre>
   # ⇓
   <pre style="color: gray">
   one <s style="color: red">too </s><b style="color: green">two </b>three.
   </pre>
   """).strip()
   # Create a line of "one " that has a "too " removed and a "two " added and ends with "three."
   line = Line.keep("one ").remove("too ").add("two ").keep_part("three.")
   # Render the line as markdown
   markdown = MarkdownPrinter.render_line(line)
   # Verify that the rendered markdown is equal to the expected markdown
   assert markdown == expected_markdown


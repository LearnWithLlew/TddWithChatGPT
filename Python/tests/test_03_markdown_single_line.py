


def test_create_markdown():
   """
   <pre style="color: gray">
   one <b style="color: red">too </b>three.
   </pre>
   # ⇓
   <pre style="color: gray">
   one <s style="color: red">too </s><b style="color: green">two </b>three.
   </pre>
   """.strip()
   # Create a line of "one " that has a "too " removed and a "two " added and ends with "three."
   # Render the line as markdown
   # Verify that the rendered markdown is equal to the expected markdown


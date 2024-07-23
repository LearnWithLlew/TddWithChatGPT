from textwrap import dedent

from project.line import Line


class MarkdownRenderer:
   @staticmethod
   def render(line):
      original_parts = []
      final_parts = []
      started_removed = False

      for part in line.parts:
         if part.is_unchanged():
            original_parts.append(f'{part.text}')
            final_parts.append(f'{part.text}')
         elif part.is_removed():
            original_parts.append(f'<b style="color: red">{part.text}</b>')
            final_parts.append(f'<s style="color: red">{part.text}</s>')
            started_removed = True
         elif part.is_added():
            if started_removed:
               final_parts.append(f'<b style="color: green">{part.text}</b>')
               started_removed = False
            else:
               original_parts.append(f'<b style="color: red">{part.text}</b>')
               final_parts.append(f'<b style="color: green">{part.text}</b>')

      original_text = ''.join(original_parts)
      final_text = ''.join(final_parts)

      return f"""
<pre style="color: gray">
{original_text}
</pre>
# ⇓
<pre style="color: gray">
{final_text}
</pre>
        """.strip()


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
   line = Line().keep("one ").remove("too ").add("two ").keep("three.")
   rendered_markdown = MarkdownRenderer.render(line)
   assert rendered_markdown == expected_markdown




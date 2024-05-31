class MarkdownPrinter:
   @staticmethod
   def render_line(line):
      initial_markdown = '<pre style="color: gray">\n'
      final_markdown = '<pre style="color: gray">\n'

      for part in line.get_parts():
         if part.is_unchanged():
            initial_markdown += part.text
            final_markdown += part.text
         elif part.is_removed():
            initial_markdown += f'<b style="color: red">{part.text}</b>'
            final_markdown += f'<s style="color: red">{part.text}</s>'
         elif part.is_added():
            final_markdown += f'<b style="color: green">{part.text}</b>'

      initial_markdown += '\n</pre>'
      final_markdown += '\n</pre>'

      combined_markdown = f'{initial_markdown}\n# ⇓\n{final_markdown}'
      return combined_markdown

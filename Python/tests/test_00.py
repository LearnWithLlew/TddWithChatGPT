import difflib


class Diff:
    @staticmethod
    def of(str1, str2):
        # Use difflib to find differences
        d = difflib.Differ()
        diff = list(d.compare(str1.splitlines(), str2.splitlines()))
        return diff


class MarkdownRender:
    @staticmethod
    def refactoringsOf(diff_lines):
        old_version = []
        new_version = []

        for line in diff_lines:
            if line.startswith('  '):
                old_version.append(line[2:])
                new_version.append(line[2:])
            elif line.startswith('- '):
                old_version.append(f"<b style='color: red'>{line[2:]}</b>")
                new_version.append(f"<s style='color: red'>{line[2:]}</s>")
            elif line.startswith('+ '):
                new_version.append(f"<b style='color: green'>{line[2:]}</b>")

        old_version = "\n".join(old_version)
        new_version = "\n".join(new_version)

        markdown = (
            f"<pre style='color: gray'>\n{old_version}\n</pre>\n"
            f"# ⇓\n"
            f"<pre style='color: gray'>\n{new_version}\n</pre>"
        )

        return markdown

def test_something():
    # Example usage:
    lines = Diff.of("Start\nOne too three.\nEnd", "Start\nOne two three.\nEnd")
    markdown = MarkdownRender.refactoringsOf(lines)
    print(markdown)

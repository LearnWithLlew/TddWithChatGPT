from project.line import Line
from project.part import Part

class Diff:
    @staticmethod
    def create(text1, text2):
        words1 = text1.split(' ')
        words2 = text2.split(' ')
        line = Line()

        i, j = 0, 0
        while i < len(words1) and j < len(words2):
            if words1[i] == words2[j]:
                line.keep(words1[i] + " ")
                i += 1
                j += 1
            else:
                line.remove(words1[i] + " ")
                line.add(words2[j] + " ")
                i += 1
                j += 1

        while i < len(words1):
            line.remove(words1[i] + " ")
            i += 1

        while j < len(words2):
            line.add(words2[j] + " ")
            j += 1

        # Remove trailing space from the last part
        if line.parts:
            line.parts[-1].text = line.parts[-1].text.rstrip()

        return line

def test_create_diff():
    line = Diff.create("one too three.", "one two three.")
    assert str(line) == "`one `[unchanged], `too `[removed], `two `[added], `three.`[unchanged]"

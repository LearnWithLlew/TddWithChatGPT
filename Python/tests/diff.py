from tests.line import Line


class Diff:
    @staticmethod
    def of(old_text, new_text):
        old_words = old_text.split()
        new_words = new_text.split()
        line = Line()

        i, j = 0, 0
        while i < len(old_words) and j < len(new_words):
            if old_words[i] == new_words[j]:
                line.keep_part(old_words[i] + (" " if i < len(old_words) - 1 else ""))
                i += 1
                j += 1
            else:
                if old_words[i] not in new_words:
                    line.remove(old_words[i] + (" " if i < len(old_words) - 1 else ""))
                    i += 1
                elif new_words[j] not in old_words:
                    line.add(new_words[j] + (" " if j < len(new_words) - 1 else ""))
                    j += 1
                else:
                    line.remove(old_words[i] + (" " if i < len(old_words) - 1 else ""))
                    line.add(new_words[j] + (" " if j < len(new_words) - 1 else ""))
                    i += 1
                    j += 1

        while i < len(old_words):
            line.remove(old_words[i] + (" " if i < len(old_words) - 1 else ""))
            i += 1

        while j < len(new_words):
            line.add(new_words[j] + (" " if j < len(new_words) - 1 else ""))
            j += 1

        return line

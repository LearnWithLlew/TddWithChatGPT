from tests.line import Line


class Diff:
    @staticmethod
    def compare(originalText, newText):
        originalWords = originalText.split()
        newWords = newText.split()
        lineDiff = Line()

        originalIndex, newIndex = 0, 0
        while originalIndex < len(originalWords) and newIndex < len(newWords):
            if originalWords[originalIndex] == newWords[newIndex]:
                lineDiff.keep_part(originalWords[originalIndex] + (" " if originalIndex < len(originalWords) - 1 else ""))
                originalIndex += 1
                newIndex += 1
            else:
                if originalWords[originalIndex] not in newWords:
                    lineDiff.remove(originalWords[originalIndex] + (" " if originalIndex < len(originalWords) - 1 else ""))
                    originalIndex += 1
                elif newWords[newIndex] not in originalWords:
                    lineDiff.add(newWords[newIndex] + (" " if newIndex < len(newWords) - 1 else ""))
                    newIndex += 1
                else:
                    lineDiff.remove(originalWords[originalIndex] + (" " if originalIndex < len(originalWords) - 1 else ""))
                    lineDiff.add(newWords[newIndex] + (" " if newIndex < len(newWords) - 1 else ""))
                    originalIndex += 1
                    newIndex += 1

        while originalIndex < len(originalWords):
            lineDiff.remove(originalWords[originalIndex] + (" " if originalIndex < len(originalWords) - 1 else ""))
            originalIndex += 1

        while newIndex < len(newWords):
            lineDiff.add(newWords[newIndex] + (" " if newIndex < len(newWords) - 1 else ""))
            newIndex += 1

        return lineDiff

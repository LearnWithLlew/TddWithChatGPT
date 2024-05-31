from tests.line import Line


class Diff:
    @staticmethod
    def compare(originalText, newText):
        originalWords = originalText.split()
        newWords = newText.split()
        lineDiff = Line()

        originalIndex, newIndex = 0, 0
        newIndex = Diff.process_all_words(lineDiff, newIndex, newWords, originalIndex, originalWords)

        while newIndex < len(newWords):
            lineDiff.add(newWords[newIndex] + (" " if newIndex < len(newWords) - 1 else ""))
            newIndex += 1

        return lineDiff

    @staticmethod
    def process_all_words(lineDiff, newIndex, newWords, originalIndex, originalWords):
        while originalIndex < len(originalWords) and newIndex < len(newWords):
            if originalWords[originalIndex] == newWords[newIndex]:
                lineDiff.keep_part(
                    originalWords[originalIndex] + (" " if originalIndex < len(originalWords) - 1 else ""))
                originalIndex += 1
                newIndex += 1
            else:
                if originalWords[originalIndex] not in newWords:
                    lineDiff.remove(
                        originalWords[originalIndex] + (" " if originalIndex < len(originalWords) - 1 else ""))
                    originalIndex += 1
                elif newWords[newIndex] not in originalWords:
                    lineDiff.add(newWords[newIndex] + (" " if newIndex < len(newWords) - 1 else ""))
                    newIndex += 1
                else:
                    newIndex, originalIndex = Diff.process_changed_words(lineDiff, newIndex, newWords, originalIndex,
                                                                         originalWords)
        Diff.process_remaining_original_words(lineDiff, originalIndex, originalWords)
        return newIndex

    @staticmethod
    def process_changed_words(lineDiff, newIndex, newWords, originalIndex, originalWords):
        lineDiff.remove(originalWords[originalIndex] + (" " if originalIndex < len(originalWords) - 1 else ""))
        lineDiff.add(newWords[newIndex] + (" " if newIndex < len(newWords) - 1 else ""))
        originalIndex += 1
        newIndex += 1
        return newIndex, originalIndex

    @staticmethod
    def process_remaining_original_words(lineDiff, originalIndex, originalWords):
        while originalIndex < len(originalWords):
            lineDiff.remove(originalWords[originalIndex] + (" " if originalIndex < len(originalWords) - 1 else ""))
            originalIndex += 1

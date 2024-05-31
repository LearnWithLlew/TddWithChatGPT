from tests.part import Part


class Line:
    def __init__(self):
        self.parts = []

    @staticmethod
    def keep(text):
        line = Line()
        line.parts.append(Part(text, "unchanged"))
        return line

    def remove(self, text):
        self.parts.append(Part(text, "removed"))
        return self

    def add(self, text):
        self.parts.append(Part(text, "added"))
        return self

    def keep_part(self, text):
        self.parts.append(Part(text, "unchanged"))
        return self

    def get_parts(self):
        return self.parts

    def __str__(self):
        return ", ".join(str(part) for part in self.parts)

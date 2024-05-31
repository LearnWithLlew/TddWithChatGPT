from tests.Part import Part


class Line:
    def __init__(self, parts):
        self.parts = parts

    @staticmethod
    def of(text):
        return Line([Part(text, 'unchanged')])

    def remove(self, text):
        for part in self.parts:
            if part.text == text:
                part.state = 'removed'
        return self

    def add(self, text):
        self.parts.append(Part(text, 'added'))
        return self

    def get_parts(self):
        return self.parts

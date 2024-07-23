from project.part import Part


class Line:



    def __init__(self):
        self.parts = []

    def keep(self, text):
        self.parts.append(Part(text, 'unchanged'))
        return self

    def remove(self, text):
        self.parts.append(Part(text, 'removed'))
        return self

    def add(self, text):
        self.parts.append(Part(text, 'added'))
        return self

    def __str__(self):
        return ', '.join([str(part) for part in self.parts])
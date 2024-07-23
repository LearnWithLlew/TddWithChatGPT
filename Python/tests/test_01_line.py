class Line:
    class Part:
        def __init__(self, text, change_type):
            self.text = text
            self.change_type = change_type

        def is_unchanged(self):
            return self.change_type == 'unchanged'

        def is_removed(self):
            return self.change_type == 'removed'

        def is_added(self):
            return self.change_type == 'added'

    def __init__(self):
        self.parts = []

    def keep(self, text):
        self.parts.append(Line.Part(text, 'unchanged'))
        return self

    def remove(self, text):
        self.parts.append(Line.Part(text, 'removed'))
        return self

    def add(self, text):
        self.parts.append(Line.Part(text, 'added'))
        return self

def test_simple_replace():
    line = Line().keep("one ").remove("too ").add("two ").keep("three.")
    assert line.parts[0].is_unchanged()
    assert line.parts[1].is_removed()
    assert line.parts[2].is_added()
    assert line.parts[3].is_unchanged()


def test_to_string():
    # Create a line of "one " that has a "too " removed and a "two " added and ends with "three."
    # Check that the line is equal to "`one `[unchanged], `too `[removed], `two `[added], `three.`[unchanged]"
    pass



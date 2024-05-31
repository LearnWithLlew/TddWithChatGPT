class Part:
    def __init__(self, text, status):
        self.text = text
        self.status = status

    def is_unchanged(self):
        return self.status == "unchanged"

    def is_removed(self):
        return self.status == "removed"

    def is_added(self):
        return self.status == "added"

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

def test_simple_replace():
    # Create a line of "one " that has a "too " removed and a "two " added and ends with "three."
    line = Line.keep("one ").remove("too ").add("two ").keep_part("three.")

    # Check that first parts of the line is unchanged
    assert line.get_parts()[0].is_unchanged()
    # Check that second parts of the line is removed
    assert line.get_parts()[1].is_removed()
    # Check that third parts of the line is added
    assert line.get_parts()[2].is_added()
    # Check that fourth parts of the line is unchanged
    assert line.get_parts()[3].is_unchanged()

def test_to_string():
    # Create a line of "one " that has a "too " removed and a "two " added and ends with "three."
    # Check that the line is equal to "`one `[unchanged], `too `[removed], `two `[added], `three.`[unchanged]"
    pass
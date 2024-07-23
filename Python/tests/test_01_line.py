from project.line import Line


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



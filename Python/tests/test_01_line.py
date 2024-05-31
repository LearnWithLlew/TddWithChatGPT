from tests.line import Line


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
    line = Line.keep("one ").remove("too ").add("two ").keep_part("three.")
    # Check that the line is equal to "`one `[unchanged], `too `[removed], `two `[added], `three.`[unchanged]"
    assert str(line) == "`one `[unchanged], `too `[removed], `two `[added], `three.`[unchanged]"
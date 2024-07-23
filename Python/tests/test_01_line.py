from project.line import Line


def test_simple_replace():
    line = Line().keep("one ").remove("too ").add("two ").keep("three.")
    assert line.parts[0].is_unchanged()
    assert line.parts[1].is_removed()
    assert line.parts[2].is_added()
    assert line.parts[3].is_unchanged()


def test_to_string():
    line = Line().keep("one ").remove("too ").add("two ").keep("three.")
    assert str(line) == "`one `[unchanged], `too `[removed], `two `[added], `three.`[unchanged]"



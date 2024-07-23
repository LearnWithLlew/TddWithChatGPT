from project.diff import Diff


def test_create_diff():
    line = Diff.create("one too three.", "one two three.")
    assert str(line) == "`one `[unchanged], `too `[removed], `two `[added], `three.`[unchanged]"

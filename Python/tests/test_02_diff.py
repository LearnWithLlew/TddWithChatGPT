from tests.diff import Diff


def test_create_diff():
    # Diff the line "one too three." with "one two three."
    line = Diff.of("one too three.", "one two three.")
    # Check that the line is equal to "`one `[unchanged], `too `[removed], `two `[added], `three.`[unchanged]"
    assert str(line) == "`one `[unchanged], `too `[removed], `two `[added], `three.`[unchanged]"

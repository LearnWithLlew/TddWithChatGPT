package org.samples;


import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class LineTest {

    @Test
    public void testSimpleReplace() {
        // Create a line of "one " that has a "too " removed and a "two " added and ends with "three."
        Line line = Line.keep("one ").remove("too ").add("two ").keepPart("three.");

        // Check that first parts of the line is unchanged
        assertTrue(line.getParts().get(0).isUnchanged());
        // Check that second parts of the line is removed
        assertTrue(line.getParts().get(1).isRemoved());
        // Check that third parts of the line is added
        assertTrue(line.getParts().get(2).isAdded());
        // Check that fourth parts of the line is unchanged
        assertTrue(line.getParts().get(3).isUnchanged());
    }

    @Test
    public void testToString() {
        // Create a line of "one " that has a "too " removed and a "two " added and ends with "three."
        Line line = Line.keep("one ").remove("too ").add("two ").keepPart("three.");
        // Check that the line is equal to "`one `[unchanged], `too `[removed], `two `[added], `three.`[unchanged]"
        assertEquals("`one `[unchanged], `too `[removed], `two `[added], `three.`[unchanged]", line.toString());
    }
}

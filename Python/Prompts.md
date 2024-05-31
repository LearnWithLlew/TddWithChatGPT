## Prompt 1 - Zero Shot

Please write some java code that will compare two string, 
and return a list of the differences between the two strings.

I would like the API to be as follows:

```java
Line[] lines = Diff.of("Start\nOne too three.\nEnd", "Start\nOne two three.\n");
String markdown = MarkdownRender.refactoringsOf(lines);
```

Which would produce:
```markdown
<pre style="color: gray">
Start
One <b style="color: red">too </b>three.
End
</pre>
# ⇓
<pre style="color: gray">
Start
One <s style="color: red">too </s><b style="color: green">two </b>three.
End
</pre>
```

<pre style="color: gray">
Start
One <b style="color: red">too </b>three.
End
</pre>
# ⇓
<pre style="color: gray">
Start
One <s style="color: red">too </s><b style="color: green">two </b>three.
End
</pre>

## Prompt 2 - Smaller Zero Shot

 # Overview

|       |                |
|-------|----------------|
| start | one too three. |
| end   | one two three. |

Give a starting line, and an ending line, 
I would like to be able to describe the changes between the two lines.
Please write a python implementation of the Line class

### Desired API

```python
line = Line.compare("one ").removed("too ").added("two "). and ("three.")
```


### Additional Requirements

Please make the Line class immutable. 
If the state needs to change, create a new instance of that class.
Also, please design to the class to be dynamic with the number of 
changes that might occur in a line.

## Prompt 3 - TDD

```python
line = Line.compare("one ").removed("too ").added("two "). and ("three.")
assert line.get_parts()[0].is_same() == True
assert line.get_parts()[1].is_removed() == True
assert line.get_parts()[2].is_added() == True
assert line.get_parts()[3].is_same() == True
```

# Prompt 4 - Markdown Render


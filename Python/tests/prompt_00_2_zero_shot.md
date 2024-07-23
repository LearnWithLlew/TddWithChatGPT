Please write some python code that will compare two string, 
and return a list of the differences between the two strings.

I would like the API to be as follows:

```python
lines = Diff.of("Start\nOne too three.\nEnd", "Start\nOne two three.\nEnd")
markdown = MarkdownRender.refactoringsOf(lines)
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
<b style="color: red">One too three.</b>
End
</pre>
# ⇓
<pre style="color: gray">
Start
<s style="color: red">One too three.</s>
<b style="color: green">One two three.</b>
End
</pre>
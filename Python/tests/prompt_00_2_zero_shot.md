Please write some python code that will compare two string, 
and return a list of the differences between the two strings.

I would like the API to be as follows:

```python
lines = Diff.of("Start\nOne too three.\nEnd", "Start\nOne two three.\nEnd")
markdown = MarkdownRender.refactoringsOf(lines)
```

Which would produce:
```markdown

```



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

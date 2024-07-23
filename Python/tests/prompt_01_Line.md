You are an expert in python.

# Process

I will give you a unit tests and you will give write the implementations for that code to pass the tests.
just show me the code, no explanations

# Next Steps
If this makes sense please respond with `show me the code`


```mermaid
classDiagram
    class Line {
        +List~Part~ parts
        +keep(text: str) Line
        +remove(text: str) Line
        +add(text: str) Line
        +__str__() str
    }
    class Part {
        +text: str
        +change_type: str
        +is_unchanged() bool
        +is_removed() bool
        +is_added() bool
        +__str__() str
    }
    Line --> Part
```
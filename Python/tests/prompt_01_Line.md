You are an expert in python.

# Process

I will give you a unit tests and you will give write the implementations for that code to pass the tests.
just show me the code, no explanations

# Next Steps
If this makes sense please respond with `show me the code`


```mermaid
classDiagram
    class Part {
        -String text
        -String status
        +__init__(text: String, status: String)
        +is_unchanged(): bool
        +is_removed(): bool
        +is_added(): bool
        +__str__(): String
    }

    class Line {
        -List~Part~ parts
        +__init__()
        +keep(text: String): Line
        +remove(text: String): Line
        +add(text: String): Line
        +keep_part(text: String): Line
        +get_parts(): List~Part~
        +__str__(): String
    }
    
    Line "1" *-- "0..*" Part

```
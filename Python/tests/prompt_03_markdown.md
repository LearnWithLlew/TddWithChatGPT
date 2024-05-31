``````mermaid
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
    
    class Diff {
        +static of(old_text: String, new_text: String): Line
    }

    class MarkdownPrinter {
        +static render(line: Line): String
    }
    
    Line "1" *-- "0..*" Part
    Diff "1" *-- "1" Line

```
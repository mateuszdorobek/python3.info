```plantuml

class Editor {
    - content: str
    + create_state()
    + restore_state(state)
}

class EditorState {
    - content: str
}

class History {
    - states: list[EditorState]
    + push(state)
    + pop()
}

EditorState <--* History : aggregates
Editor ..> EditorState : depends

```

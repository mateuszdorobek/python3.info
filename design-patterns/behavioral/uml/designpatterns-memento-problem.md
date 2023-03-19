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

EditorState -down[plain]-* History : composition
Editor -right[dashed]-> EditorState : dependency

```

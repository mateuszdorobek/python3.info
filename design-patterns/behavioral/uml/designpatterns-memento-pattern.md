```plantuml

class Originator {
    - content: str
    + create_state()
    + restore_state(state)
}

class Memento {
    - content: str
}

class Caretaker {
    - states: list[Memento]
    + push(state)
    + pop()
}

Memento <--* Caretaker : aggregates
Originator ..> Memento : depends

```

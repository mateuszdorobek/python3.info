```plantuml

class Account {
    # username: str
    # password: str
    + login(username: str, password: str) -> None
    + logout() -> None
}

class User {
    # groups: list[str] = ['user']
    + edit_profile() -> None
}

class Admin {
    # groups: list[str] = ['staff', 'admin']
    + edit_user(uid: int) -> None
    + delete_user(uid: int) -> None
}

Account <|-- User
Account <|-- Admin

note as COMMENT
    class User inherits from Account
    class Admin inherits from Account
endnote

```

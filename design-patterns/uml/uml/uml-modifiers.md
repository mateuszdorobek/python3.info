Access Modifiers
================

Public
------
```plantuml
class User {
    + firstname
    + lastname
}
```

Protected
---------
```plantuml
class User {
    # email
    # phone
}
```

Private
-------
```plantuml
class User {
    - username
    - password
}
```

Package Private
---------------
```plantuml
class User {
    ~ author
    ~ version
}
```

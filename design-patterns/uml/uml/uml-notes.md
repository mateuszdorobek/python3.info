Notes
=====

Oneline
-------
```plantuml
class User
note right: Comment
```


Multiline
---------
```plantuml
class User
note right
  Comment
  Comment
  Comment
end note
```


Directions
----------
```plantuml
class User
note left: On last defined class
```

```plantuml
class User
note right: On last defined class
```

```plantuml
class User
note top: On last defined class
```

```plantuml
class User
note bottom: On last defined class
```


Attached to One Object
----------------------
Notes attached to the particular object

```plantuml
class User

note top of User: Comment
```

```plantuml
class User

note top of User
  Comment
  Comment
  Comment
end note
```

Attached to Many Objects
------------------------
```plantuml
class User
class Admin

note "Two roles in our system" as Comment

User .. Comment
Admin .. Comment
```

Attributes
----------
```plantuml
class User {
    username: str
    password: str
}

note right of User::password
    Password will be encrypted
end note
```

Methods
-------
```plantuml
class User {
    + login()
    + logout()
}

note right of User::login
    Logs user in
end note

note right of User::logout
    Logs user out
end note
```

Relations
---------
```plantuml
class User
User <|-- Admin
note on link: Admin inherits from User
```


Floating
--------
```plantuml
class User
note "This is a floating note" as N1
```


Formatting
----------
```plantuml
class object

note top of object : "In Python, <b>every</b> class\n<u>inherits</u> from <i>object</i>."
```

```plantuml
class User
User <|-- Admin
note on link #red: Admin inherits from User
```

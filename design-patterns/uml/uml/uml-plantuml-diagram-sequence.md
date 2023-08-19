```plantuml
autonumber

actor Client
participant Server
database Database

activate Client
Client ->> Server: HTTP Request

activate Server
Server ->> Database: SQL Query

activate Database
Database -->> Server: Result
deactivate Database

Server -->> Client: HTTP Response
deactivate Server

deactivate Client
```

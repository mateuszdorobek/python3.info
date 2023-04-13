Microservice Event
==================


Event-driven Architecture
-------------------------
* Use an event-driven, eventually consistent approach. Each service
   publishes an event whenever it update it's data. Other service
   subscribe to events. When an event is received, a service updates
   it's data.


Event Sourcing
--------------
* Reliably publish events whenever state changes by using Event
   Sourcing. Event Sourcing persists each business entity as a sequence
   of events, which are replayed to reconstruct the current state.

Event sourcing:

.. figure:: img/microservices-event-sourcing.png


Application Events
------------------
* Reliably publish events whenever state changes by having the application insert events into an EVENTS table as part of the local transaction. A separate process polls the EVENTS table and publishes the events to a message broker.

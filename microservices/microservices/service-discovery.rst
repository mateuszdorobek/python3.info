Microservice Discovery
======================
* Client-side Service discovery
* Server-side Service discovery
* Service registry
* Self registration


Client-side Service discovery
-----------------------------
* When making a request to a service, the client obtains the location of a service instance by querying a Service Registry, which knows the locations of all service instances.
* Eureka is a Service Registry
* Ribbon Client is an HTTP client that queries Eureka to route HTTP requests to an available service instance

.. figure:: img/microservices-client-side-discovery.jpg

    Microservices client side discovery


Server-side Service discovery
-----------------------------
* When making a request to a service, the client makes a request via a router (a.k.a load balancer) that runs at a well known location. The router queries a service registry, which might be built into the router, and forwards the request to an available service instance.
* AWS Elastic Load Balancer (ELB), Kubernetes, Marathon

.. figure:: img/microservices-server-side-discovery.jpg

    Server side-discovery


Service registry
----------------
* Implement a service registry, which is a database of services, their instances and their locations. Service instances are registered with the service registry on startup and deregistered on shutdown. Client of the service and/or routers query the service registry to find the available instances of a service.
* Eureka, Apache Zookeeper, Consul, Etcd


Self registration
-----------------
* A service instance is responsible for registering itself with the service registry. On startup the service instance registers itself (host and IP address) with the service registry and makes itself available for discovery. The client must typically periodically renew it's registration so that the registry knows it is still alive. On shutdown, the service instance unregisters itself from the service registry.
* Apache Zookeeper, Netflix Eureka


3rd party registration
----------------------
* A 3rd party registrar is responsible for registering and unregistering a service instance with the service registry. When the service instance starts up, the registrar registers the service instance with the service registry. When the service instance shuts downs, the registrar unregisters the service instance from the service registry.
* Netflix Prana - a "side car" application that runs along side a non-JVM application and registers the application with Eureka.
* AWS Autoscaling Groups automatically (un)registers EC2 instances with Elastic Load Balancer
* Joyent's Container buddy runs in a Docker container as the parent process for the service and registers it with the registry
* Registrator - registers and unregisters Docker containers with various service registries
* Clustering frameworks such as Kubernetes and Marathon (un)register service instances with the built-in/implicit registry

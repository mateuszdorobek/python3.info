Microservice Runtime
====================
* Multiple service instances per host
* Single service instance per host
* Service instance per VM
* Service instance per Container
* Serverless deployment


Multiple service instances per host
-----------------------------------
* Run multiple instances of different services on a host (Physical or Virtual machine).
* There are various ways of deploying a service instance on a shared host including:
* Deploy each service instance as a JVM process. For example, a Tomcat or Jetty instances per service instance.
* Deploy multiple service instances in the same JVM. For example, as web applications or OSGI bundles.


Single service instance per host
--------------------------------
* Deploy each single service instance on it's own host


Service instance per VM
-----------------------
* Package the service as a virtual machine image and deploy each
   service instance as a separate VM


Service instance per Container
------------------------------
* Package the service as a (Docker) container image and deploy each service instance as a container
* Kubernetes, Marathon/Mesos, Amazon EC2 Container Service


Serverless deployment
---------------------
* Use a deployment infrastructure that hides any concept of servers (i.e. reserved or preallocated resources)- physical or virtual hosts, or containers. The infrastructure takes your service's code and runs it. You are charged for each request based on the resources consumed.
* To deploy your service using this approach, you package the code (e.g. as a ZIP file), upload it to the deployment infrastructure and describe the desired performance characteristics.
* The deployment infrastructure is a utility operated by a public cloud provider. It typically uses either containers or virtual machines to isolate the services. However, these details are hidden from you. Neither you nor anyone else in your organization is responsible for managing any low-level infrastructure such as operating systems, virtual machines, etc.
* AWS Lambda, Google Cloud Functions, Azure Functions

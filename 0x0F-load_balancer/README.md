# 0x0F. Load balancer
``DevOps`` ``SysAdmin``
## Concepts
* [Load balancer](#loadBalancer)
* [Web stack debugging](#webStackDebug)
* [Introduction to HAProxy](#introToHAProxy)

#### Load balancer
<a href='loadbalancer'></a>
Load balancer helps distribute web traffic over various server to reduce the amount of load on an individual system.

Advantages of load balancing your application:
* Reduce work load on individual server
* Large amount of work done in same time due to concurrency
* No SPOF
* When appropriate load balancing algorithm is use, it brings optimal and efficient utilization of the resources, as it eliminates the scenario of some server's resources are getting used than others.
* Scalability: We can increase or decrease the number of servers on the fly without bring down the application
* Increased Reliability
* Increased security as the physical servers and IPs are abstract in certain cases.

On a high level, there are two types of load balancers
1. Software load
2. Hardware load balancer

1. Software Load Balancers: are often installed on the servers and consumes the processor and memory of the servers. includes the Weighted Sheduling Algorithm (work is assigned according to the weight assigned to the server), Round Robin Scheduling (Requests are served by the server sequentially one after another. After sending the request to the last server, it starts from the first server again), Least Connection First Scheduling (Requests are served first to the server which is currently handling least number of persistent connections).

Load balancing softwares can have the smart implementation of the combination of any of the above three basic scheduling algorithm

Software Load Balancer Examples:
* HAProxy - A TCP load balancer
* NGINX - A http load balancer with SSL termination support
* mod athena - Apache, based http load balancer
* Varnish, Balance, LVS

2. Hardware Load Balancers: Load balancing hardwares are often referred as specialized routers or switches which are deployed in between the servers and client.<br/>
The hardware load balancers are implemented on Layer 4 (Transport layer) and Layer 7 (Application layer) of OSI model

[more examples on load-balancing Algorithm](https://community.f5.com/t5/technical-articles/intro-to-load-balancing-for-developers-ndash-the-algorithms/ta-p/273759)

#### Introduction to HAProxy and Load Balancing Concepts
<a href='introToHAProxy'></a>
HAProxy stands for Hign Availability Proxy, which is a popular open source software TCP/HTTP Load Balancer and proxying solution which can be run on Linux, macOS, and FreeBSD. Its most common use is to improve the performance and reliability of a server environment by distributing the workload accross multiple servers (ex., web, application, database).

There are many terms and concepts that are important when discussing load balancing and proxying. Before getting into the basic types of load balancing, it is good to begin with a review of ACLs, backends, and frontends.

* ACL (Access Control List)<br />
In relation to load balancing, ACLs are used to test some condition and perform an action (ex. select a server, or block a request) base on the test result. ACLs allows flexible network traffic forwarding based on a variety of factors like pattern-matching and the number of connections to a backend.
* Backend<br />
A backend is a set of servers that receives forwarded requests. Backends are defined in the backend section of the HAProxy configuration
* Frontend<br />
A frontend defines how requests should be forwarded to backends. Frontends are defined in the ``frontend`` section of the HAProxy configuration. Their definitions are composed of the following components:
* a set of IP addresses and a port
* ACLs
* use backend rules which define which backends to use depending on which ACL conditions are matched and/or a ``default_backend rule that handles every other case

**Types of Load Balancing**
* Layer 4 Load Balancing: (The simplest way to load balance network traffic to multiple servers) This will forward user traffic based on IP range and port. The user accessed the load balancer, which forwards the user's request to the web-backend group of backend servers. Whichever backend is selected will be responsible directly to the user's request.
* Layer 7 Load Balancing: (more complex way to load balance network traffic) Using layer 7 allows the load balancer to forward requests to different backend servers based on the content of the user's request. This mode allows you to run multiple web application server under the same domain and port.

**Health Check**
HAProxy uses health checks to determine if a backend server is available to process requests. This avoids having to manually remove a server from the backend if it becomes unavailable. The default health check is to try to establicsh a TCP connection to the server.<br />
If a server fails a health check, and therefore is unable to server requests, it is automatically disabled in the backend, and traffic will not be forwarded to it until it becomes  healthy again.

A load balancer facilitates redundancy for the backend layer (web/app servers), but for a true high availability setup, there is need to have redundant load balancer as well



---
title: "SoftLayer_Network_LBaaS_LoadBalancer"
description: "The SoftLayer_Network_LBaaS_LoadBalancer service allows customers to create, edit, delete, get details of a load balancer instance and retrieve all existing load balancer instances. The most common use case of a load balancer instance is to improve performance and high availability of customers application services by distributing the incoming requests across multiple servers. Thus, clients using customers application services will only need to know the load balancer instances host name respective IP address in order to submit their requests. Note that SoftLayer_Network_LBaaS_LoadBalancer provides the load balancing functionality only, while it is customers responsibility to implement their application services and deploy them to respective servers, typically virtual servers or bare metal systems hosted by IBM SoftLayer. Conceptually a load balancer instance consists of a set of listeners, also called frontends, pools, also called backends, and members (application servers). A listener (frontend) represents basically the network protocol and port for requests coming from clients applications and is always associated with a pool (backend) defined by a network protocol, port and load balancing algorithm. The pools network protocol and port specify how incoming requests will be forwarded to application servers, while the load balancing algorithm (round-robin, weighted round-robin or least connections) determines the distribution scheme of incoming requests among the members, ie application servers. Note that members of a load balancer instance are assigned implicitly to all pools (backends) of that load balancer. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancer"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Network_LBaaS_LoadBalancer"
---

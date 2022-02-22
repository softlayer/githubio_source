---
title: "SoftLayer_Network_LoadBalancer_Service"
description: "Load balancer services represent the 'routes' that the load balancer will have available to route requests. Each service has a source port (located on the load balancer itself), and a destination IP address and port. Any services that share a source port will be used as potential routes for traffic coming into the load balancer on that port.  For instance, if there are two services that both have a source port of 80, both of those services will be used as balanced servers for traffic coming into your virtual IP on port 80.  For a more complete example, consider the following scenario: 


:Virtual IP Address:  123.123.123.123
:Servers on your account:
:12.34.56.78
:23.45.67.89
:You want to set up both HTTP(port 80) and HTTPS (port 443) on each of those servers.
:You will need four services:


{| 
|-
! SourcePort
! DestinationIpAddress
! DestinationPort
|-
| 80
| 12.34.56.78
| 80
|-
| 80
| 23.45.67.89
| 80
|-
| 443
| 12.34.56.78
| 443
|-
| 443
| 23.45.67.89
| 443
|}


The services also have a routing type, these ALSO need to be the same for services that share the same port. For this example, the services with a source port of 80 should have HTTP as their type.  The other two services should have TCP as their type. 

The affect of other variables are listed in their individual documentation. "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Service"
type: "reference"
layout: "service"
mainService : "SoftLayer_Network_LoadBalancer_Service"
---

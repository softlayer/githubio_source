---
title: "updateLoadBalancerProtocols"
description: "Update (create) load balancers front- and backend protocols and return load balancer object with listeners (frontend), p... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_Listener"
aliases:
    - "/reference/services/softlayer_network_lbaas_listener/updateLoadBalancerProtocols"
---
# [SoftLayer_Network_LBaaS_Listener](/reference/services/SoftLayer_Network_LBaaS_Listener)::updateLoadBalancerProtocols

Update/create load balancers protocols


## Overview 
Update (create) load balancers front- and backend protocols and return load balancer object with listeners (frontend), pools (backend), server instances (members) and datacenter populated. Note if a protocolConfiguration has no listenerUuid set, this function will create the specified front- and backend accordingly. Otherwise the given front- and backend will be updated with the new protocol and port. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancerUuid| string| |
|protocolConfigurations| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration'>SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration[] </a>| |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_LBaaS_ListenerObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>


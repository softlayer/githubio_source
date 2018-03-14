---
title: "updateLoadBalancerHealthMonitors"
description: "Update load balancers health monitor and return load balancer object with listeners (frontend), pools (backend), health... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_HealthMonitor"
aliases:
    - "/reference/services/softlayer_network_lbaas_healthmonitor/updateLoadBalancerHealthMonitors"
---
# [SoftLayer_Network_LBaaS_HealthMonitor](/reference/services/SoftLayer_Network_LBaaS_HealthMonitor)::updateLoadBalancerHealthMonitors

Update load balancer health monitors


## Overview 
Update load balancers health monitor and return load balancer object with listeners (frontend), pools (backend), health monitor server instances (members) and datacenter populated 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancerUuid| string| |
|healthMonitorConfigurations| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancerHealthMonitorConfiguration'>SoftLayer_Network_LBaaS_LoadBalancerHealthMonitorConfiguration[] </a>| |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_LBaaS_HealthMonitorObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>


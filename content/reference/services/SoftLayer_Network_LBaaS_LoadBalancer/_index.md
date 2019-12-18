---
title: "SoftLayer_Network_LBaaS_LoadBalancer"
description: "The SoftLayer_Network_LBaaS_LoadBalancer service allows customers to create, edit, delete, get details of a load balance... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancer"
---
# SoftLayer_Network_LBaaS_LoadBalancer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_LoadBalancer' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Network_LBaaS_LoadBalancer service allows customers to create, edit, delete, get details of a load balancer instance and retrieve all existing load balancer instances. The most common use case of a load balancer instance is to improve performance and high availability of customers application services by distributing the incoming requests across multiple servers. Thus, clients using customers application services will only need to know the load balancer instances host name respective IP address in order to submit their requests. Note that SoftLayer_Network_LBaaS_LoadBalancer provides the load balancing functionality only, while it is customers responsibility to implement their application services and deploy them to respective servers, typically virtual servers or bare metal systems hosted by IBM SoftLayer. Conceptually a load balancer instance consists of a set of listeners, also called frontends, pools, also called backends, and members (application servers). A listener (frontend) represents basically the network protocol and port for requests coming from clients applications and is always associated with a pool (backend) defined by a network protocol, port and load balancing algorithm. The pools network protocol and port specify how incoming requests will be forwarded to application servers, while the load balancing algorithm (round-robin, weighted round-robin or least connections) determines the distribution scheme of incoming requests among the members, ie application servers. Note that members of a load balancer instance are assigned implicitly to all pools (backends) of that load balancer. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [cancelLoadBalancer](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/cancelLoadBalancer)
Cancel the specified load balancer. 

#### [enableOrDisableDataLogs](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/enableOrDisableDataLogs)
Enable or disable data logs forwarding. 

#### [getAllObjects](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getAllObjects)
Get all existing load balancers. 

#### [getDatacenter](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getDatacenter)
Retrieve datacenter, where load balancer is located.

#### [getHealthMonitors](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getHealthMonitors)
Retrieve health monitors for the backend members.

#### [getL7Pools](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getL7Pools)
Retrieve l7Pools for load balancer.

#### [getListenerTimeSeriesData](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getListenerTimeSeriesData)
Return time series datapoints

#### [getListeners](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getListeners)
Retrieve listeners assigned to load balancer.

#### [getLoadBalancer](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getLoadBalancer)
Get a specific load balancer. 

#### [getLoadBalancerMemberHealth](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getLoadBalancerMemberHealth)
Return load balancer members health

#### [getLoadBalancerStatistics](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getLoadBalancerStatistics)
Return load balancers statistics

#### [getMembers](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getMembers)
Retrieve members assigned to load balancer.

#### [getObject](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getObject)
Retrieve a SoftLayer_Network_LBaaS_LoadBalancer record.

#### [getSslCiphers](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/getSslCiphers)
Retrieve list of preferred custom ciphers configured for the load balancer.

#### [serviceLoadBalancer](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/serviceLoadBalancer)
Service function for a load balancer. 

#### [updateLoadBalancer](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/updateLoadBalancer)
Update a load balancer's description.

#### [updateSslCiphers](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/updateSslCiphers)
Updates the cipher list of the load balancer

</div>


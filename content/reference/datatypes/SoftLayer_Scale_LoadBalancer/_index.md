---
title: "SoftLayer_Scale_LoadBalancer"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_LoadBalancer"
---

# SoftLayer_Scale_LoadBalancer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_LoadBalancer' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_LoadBalancer' >Datatype</a></li>
    </ul>
</div>

## Description 






<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
-----
[createDate]: #createdate
#### [createDate]
When this load balancer configuration was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[deleteFlag]: #deleteflag
#### [deleteFlag]
When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.   
<span class="type-label">Type: </span>**boolean**

-----
[healthCheckId]: #healthcheckid
#### [healthCheckId]
The identifier for the health check of this load balancer configuration  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
The load balancer configuration's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
When this load balancer configuration was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[port]: #port
#### [port]
The port for this load balancer configuration.  
<span class="type-label">Type: </span>**integer**

-----
[scaleGroupId]: #scalegroupid
#### [scaleGroupId]
The identifier of the group this load balancer configuration applies to.  
<span class="type-label">Type: </span>**integer**

-----
[virtualServerId]: #virtualserverid
#### [virtualServerId]
The identifier of the virtual server this load balancer configuration uses.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[allocationPercent]: #allocationpercent
#### [allocationPercent]
The percentage of connections allocated to this virtual server.  
<span class="type-label">Type: </span>**integer**

-----
[healthCheck]: #healthcheck
#### [healthCheck]
The health check for this configuration.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check </a>**

-----
[routingMethod]: #routingmethod
#### [routingMethod]
The routing method.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method </a>**

-----
[routingType]: #routingtype
#### [routingType]
The routing type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type </a>**

-----
[scaleGroup]: #scalegroup
#### [scaleGroup]
The group this load balancer configuration is for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Group'>SoftLayer_Scale_Group </a>**

-----
[virtualIpAddressId]: #virtualipaddressid
#### [virtualIpAddressId]
The ID of the virtual IP address.  
<span class="type-label">Type: </span>**integer**

-----
[virtualServer]: #virtualserver
#### [virtualServer]
The virtual server for this configuration.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer </a>**

-----
[virtualServerPort]: #virtualserverport
#### [virtualServerPort]
The port on the virtual server.  
<span class="type-label">Type: </span>**integer**


## Count
</div>



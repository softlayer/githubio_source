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








<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
When this load balancer configuration was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[deleteFlag]: #deleteflag
#### [deleteFlag]
When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[healthCheckId]: #healthcheckid
#### [healthCheckId]
The identifier for the health check of this load balancer configuration  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The load balancer configuration's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
When this load balancer configuration was last modified.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[port]: #port
#### [port]
The port for this load balancer configuration.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[scaleGroupId]: #scalegroupid
#### [scaleGroupId]
The identifier of the group this load balancer configuration applies to.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[virtualServerId]: #virtualserverid
#### [virtualServerId]
The identifier of the virtual server this load balancer configuration uses.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[allocationPercent]: #allocationpercent
#### [allocationPercent]
The percentage of connections allocated to this virtual server.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[healthCheck]: #healthcheck
#### [healthCheck]
The health check for this configuration.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check </a>**  



</div>
<div class="prop-row">

-----
[routingMethod]: #routingmethod
#### [routingMethod]
The routing method.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method </a>**  



</div>
<div class="prop-row">

-----
[routingType]: #routingtype
#### [routingType]
The routing type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type </a>**  



</div>
<div class="prop-row">

-----
[scaleGroup]: #scalegroup
#### [scaleGroup]
The group this load balancer configuration is for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Group'>SoftLayer_Scale_Group </a>**  



</div>
<div class="prop-row">

-----
[virtualIpAddressId]: #virtualipaddressid
#### [virtualIpAddressId]
The ID of the virtual IP address.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[virtualServer]: #virtualserver
#### [virtualServer]
The virtual server for this configuration.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer </a>**  



</div>
<div class="prop-row">

-----
[virtualServerPort]: #virtualserverport
#### [virtualServerPort]
The port on the virtual server.  
<span class="type-label">Type: </span>**integer**  



</div>

## Count
</div>



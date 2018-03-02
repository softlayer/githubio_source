---
title: "SoftLayer_Network_LoadBalancer_Service"
description: "Load balancer services represent the 'routes' that the load balancer will have available to route requests. Each service... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Service"
---
# SoftLayer_Network_LoadBalancer_Service
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LoadBalancer_Service' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Service' >Datatype</a></li>
    </ul>
</div>

## Description
Load balancer services represent the "routes" that the load balancer will have available to route requests. Each service has a source port (located on the load balancer itself), and a destination IP address and port. Any services that share a source port will be used as potential routes for traffic coming into the load balancer on that port.  For instance, if there are two services that both have a source port of 80, both of those services will be used as balanced servers for traffic coming into your virtual IP on port 80.  For a more complete example, consider the following scenario: 


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

The affect of other variables are listed in their individual documentation. 



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Service/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete this service, removing it from the load balancer.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Service/getGraphImage'> getGraphImage</a> </span>
            <div class='views-field-body'>Get the connection or status graph image for a load balancer service.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Service/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_LoadBalancer_Service record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Service/getStatus'> getStatus</a> </span>
            <div class='views-field-body'>Returns various status entries for this service as an array of SoftLayer_Container_Network_LoadBalancer_StatusEntry objects</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Service/getVip'> getVip</a> </span>
            <div class='views-field-body'>Retrieve the load balancer that this service belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Service/resetPeakConnections'> resetPeakConnections</a> </span>
            <div class='views-field-body'>Update the PeakConnections value on the service to zero.</div>
        </div>
        </div>
</div>


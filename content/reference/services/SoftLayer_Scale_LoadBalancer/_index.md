---
title: "SoftLayer_Scale_LoadBalancer"
description: "A scale load balancer is a configuration for a load balancer virtual server that autoscaled members will be automaticall... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
A scale load balancer is a configuration for a load balancer virtual server that autoscaled members will be automatically configured for. 
        
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_LoadBalancer/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a load balancer for a scale group. Once created, the configuration will be used to configure the load balancers for autoscaled members. 

If the given virtual server port exists for the given virtual IP address, it is reused here if all the other values match. Otherwise, the virtual server port will be created. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_LoadBalancer/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete this load balancer configuration. Note, this does not affect existing scaled members. Once deleted however, future scaled members will not be load balanced with this configuration. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_LoadBalancer/editObject'> editObject</a> </span>
            <div class='views-field-body'>Delete this load balancer configuration. Note, this does not affect existing scaled members. Once edited however, future scaled members will be load balanced with this configuration. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_LoadBalancer/getAllocationPercent'> getAllocationPercent</a> </span>
            <div class='views-field-body'>Retrieve the percentage of connections allocated to this virtual server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_LoadBalancer/getHealthCheck'> getHealthCheck</a> </span>
            <div class='views-field-body'>Retrieve the health check for this configuration.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_LoadBalancer/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Scale_LoadBalancer record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_LoadBalancer/getRoutingMethod'> getRoutingMethod</a> </span>
            <div class='views-field-body'>Retrieve the routing method.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_LoadBalancer/getRoutingType'> getRoutingType</a> </span>
            <div class='views-field-body'>Retrieve the routing type.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_LoadBalancer/getScaleGroup'> getScaleGroup</a> </span>
            <div class='views-field-body'>Retrieve the group this load balancer configuration is for.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_LoadBalancer/getVirtualIpAddressId'> getVirtualIpAddressId</a> </span>
            <div class='views-field-body'>Retrieve the ID of the virtual IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_LoadBalancer/getVirtualServer'> getVirtualServer</a> </span>
            <div class='views-field-body'>Retrieve the virtual server for this configuration.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_LoadBalancer/getVirtualServerPort'> getVirtualServerPort</a> </span>
            <div class='views-field-body'>Retrieve the port on the virtual server.</div>
        </div>
        </div>
</div>


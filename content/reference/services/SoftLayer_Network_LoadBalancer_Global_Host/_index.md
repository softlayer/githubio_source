---
title: "SoftLayer_Network_LoadBalancer_Global_Host"
description: "Every global load balancer account contains hosts that make up the load balancing pool.  The global load balancers selec... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Host"
---
# SoftLayer_Network_LoadBalancer_Global_Host
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Host' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Host' >Datatype</a></li>
    </ul>
</div>

## Description
Every global load balancer account contains hosts that make up the load balancing pool.  The global load balancers select hosts from this pool and return the destination IP in the DNS response.  The SoftLayer_Network_LoadBalancer_Global_Host service represent these hosts. 

Hosts can only be created or modified by using the [[SoftLayer_Network_LoadBalancer_Global_Account::editObject]] method. 

Each account has a limited number of hosts that can be added to the load balancing pool, which is defined by the allowedNumberOfHosts property on a global load balancer account. 
        
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Host/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Remove a host from the load balancing pool of a global load balancer account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Host/getLoadBalancerAccount'> getLoadBalancerAccount</a> </span>
            <div class='views-field-body'>Retrieve the global load balancer account a host belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Host/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_LoadBalancer_Global_Host record.</div>
        </div>
        </div>
</div>


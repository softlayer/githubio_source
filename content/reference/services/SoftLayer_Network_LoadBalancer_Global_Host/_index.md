---
title: "SoftLayer_Network_LoadBalancer_Global_Host"
description: "The global load balancer service has been deprecated and is no longer available. 

Every global load balancer account co... "
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

<div class="deprecated"><span class="deprecation-label">Deprecated  </span></div>

The global load balancer service has been deprecated and is no longer available. 

Every global load balancer account contains hosts that make up the load balancing pool.  The global load balancers select hosts from this pool and return the destination IP in the DNS response.  The SoftLayer_Network_LoadBalancer_Global_Host service represent these hosts. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row deprecated">

#### [deleteObject](/reference/services/SoftLayer_Network_LoadBalancer_Global_Host/deleteObject)
[Deprecated] Remove a host from the load balancing pool of a global load balancer account.

<span class="deprecation-label">Deprecated  </span>


</div>

<div class="method-row">

#### [getLoadBalancerAccount](/reference/services/SoftLayer_Network_LoadBalancer_Global_Host/getLoadBalancerAccount)
Retrieve the global load balancer account a host belongs to.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_LoadBalancer_Global_Host/getObject)
Retrieve a SoftLayer_Network_LoadBalancer_Global_Host record.

</div>
</div>

</div>


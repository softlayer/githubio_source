---
title: "SoftLayer_Network_LBaaS_Listener"
description: "The SoftLayer_Network_LBaaS_Listener API service allows consumers to add, edit and delete load balancers protocols for f... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_Listener"
---
# SoftLayer_Network_LBaaS_Listener
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_Listener' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_Listener' >Datatype</a></li>
    </ul>
</div>

## Description


The SoftLayer_Network_LBaaS_Listener API service allows consumers to add, edit and delete load balancers protocols for front- and backends. In order to retrieve list of front- and backends protocols please refer to [SoftLayer_Network_LBaaS_LoadBalancer]({{<ref "reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer">}}) service. A listener object specifies the protocol and port of allowed incoming network requests and the maximum number of accepted connections. It has references to its associated load balancer and default pool object. 



        
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

<div class="method-row">

#### [deleteLoadBalancerProtocols](/reference/services/SoftLayer_Network_LBaaS_Listener/deleteLoadBalancerProtocols)
Delete load balancers front- and backend protocols

</div>

<div class="method-row">

#### [getDefaultPool](/reference/services/SoftLayer_Network_LBaaS_Listener/getDefaultPool)


</div>

<div class="method-row">

#### [getL7Policies](/reference/services/SoftLayer_Network_LBaaS_Listener/getL7Policies)


</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_LBaaS_Listener/getObject)
Retrieve a SoftLayer_Network_LBaaS_Listener record.

</div>

<div class="method-row">

#### [updateLoadBalancerProtocols](/reference/services/SoftLayer_Network_LBaaS_Listener/updateLoadBalancerProtocols)
Update/create load balancers protocols

</div>
</div>

</div>


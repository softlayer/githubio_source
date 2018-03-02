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
The SoftLayer_Network_LBaaS_Listener API service allows consumers to add, edit and delete load balancers protocols for front- and backends. In order to retrieve list of front- and backends protocols please refer to [[SoftLayer_Network_LBaaS_LoadBalancer]] service. A listener object specifies the protocol and port of allowed incoming network requests and the maximum number of accepted connections. It has references to its associated load balancer and default pool object. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LBaaS_Listener/deleteLoadBalancerProtocols'> deleteLoadBalancerProtocols</a> </span>
            <div class='views-field-body'>Delete load balancers front- and backend protocols</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LBaaS_Listener/getDefaultPool'> getDefaultPool</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LBaaS_Listener/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_LBaaS_Listener record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LBaaS_Listener/updateLoadBalancerProtocols'> updateLoadBalancerProtocols</a> </span>
            <div class='views-field-body'>Update/create load balancers protocols</div>
        </div>
        </div>
</div>


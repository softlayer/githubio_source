---
title: "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
description: "Each SoftLayer customer that has purchased a load balancer will have one defined in the SoftLayer_Network_LoadBalancer_V... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
---
# SoftLayer_Network_LoadBalancer_VirtualIpAddress
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress' >Datatype</a></li>
    </ul>
</div>

## Description
Each SoftLayer customer that has purchased a load balancer will have one defined in the SoftLayer_Network_LoadBalancer_VirtualIpAddress service.  Load balancers have a virtual IP address and a number of SoftLayer_Network_LoadBalancer_Service objects associated with them.  The SoftLayer_Network_LoadBalancer_VirtualIpAddress object is the only way for a customer to make changes to their load balancer service. 

Load balancers can be upgraded by using the upgradeConnectionLimit function, but this will upgrade your billing accordingly.  Downgrades are currently not supported, please open a ticket to accomplish a downgrade. 
        
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/disable'> disable</a> </span>
            <div class='views-field-body'>Disable a Virtual IP Address</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit the object by passing in a modified instance of the object</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/enable'> enable</a> </span>
            <div class='views-field-body'>Enable a Virtual IP Address</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account that owns this load balancer.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the current billing item for the Load Balancer.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getCustomerManagedFlag'> getCustomerManagedFlag</a> </span>
            <div class='views-field-body'>Retrieve if false, this VIP and associated services may be edited via the portal or the API. If true, you must configure this VIP manually on the device.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getManagedResourceFlag'> getManagedResourceFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that the load balancer is a managed resource.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_LoadBalancer_VirtualIpAddress record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getServices'> getServices</a> </span>
            <div class='views-field-body'>Retrieve the services on this load balancer.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/kickAllConnections'> kickAllConnections</a> </span>
            <div class='views-field-body'>Kick all active connections off a Virtual IP Address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/upgradeConnectionLimit'> upgradeConnectionLimit</a> </span>
            <div class='views-field-body'>Upgrades the connection limit on the Virtual IP Address and changes the billing item on your account to reflect the change.</div>
        </div>
        </div>
</div>


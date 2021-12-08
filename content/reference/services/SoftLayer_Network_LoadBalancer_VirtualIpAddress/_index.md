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

#### [disable](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/disable)
Disable a Virtual IP Address

</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/editObject)
Edit the object by passing in a modified instance of the object

</div>

<div class="method-row">

#### [enable](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/enable)
Enable a Virtual IP Address

</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getAccount)
Retrieve the account that owns this load balancer.

</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getBillingItem)
Retrieve the current billing item for the Load Balancer.

</div>

<div class="method-row">

#### [getCustomerManagedFlag](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getCustomerManagedFlag)
Retrieve if false, this VIP and associated services may be edited via the portal or the API. If true, you must configure this VIP manually on the device.

</div>

<div class="method-row">

#### [getManagedResourceFlag](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getManagedResourceFlag)
Retrieve a flag indicating that the load balancer is a managed resource.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getObject)
Retrieve a SoftLayer_Network_LoadBalancer_VirtualIpAddress record.

</div>

<div class="method-row">

#### [getServices](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getServices)
Retrieve the services on this load balancer.

</div>

<div class="method-row">

#### [kickAllConnections](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/kickAllConnections)
Kick all active connections off a Virtual IP Address.

</div>

<div class="method-row">

#### [upgradeConnectionLimit](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/upgradeConnectionLimit)
Upgrades the connection limit on the Virtual IP Address and changes the billing item on your account to reflect the change.

</div>
</div>

</div>


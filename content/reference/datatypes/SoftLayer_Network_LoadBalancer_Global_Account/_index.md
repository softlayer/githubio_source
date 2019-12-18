---
title: "SoftLayer_Network_LoadBalancer_Global_Account"
description: "The SoftLayer_Network_LoadBalancer_Global_Account data type contains the properties for a single global load balancer ac... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Account"
---

# SoftLayer_Network_LoadBalancer_Global_Account
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LoadBalancer_Global_Account' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Account' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_LoadBalancer_Global_Account data type contains the properties for a single global load balancer account.  The properties you are able to edit are fallbackIp, loadBalanceTypeId, and notes. The hosts relational property can be used for creating and editing hosts that belong to the global load balancer account.  The [SoftLayer_Network_LoadBalancer_Global_Account::editObject]({{<ref "reference/services/SoftLayer_Network_LoadBalancer_Global_Account/editObject">}}) method contains details on creating and edited hosts through the hosts relational property. 


### associatedMethods

*  [SoftLayer_Account::getGlobalLoadBalancerAccounts](/reference/services/SoftLayer_Account/getGlobalLoadBalancerAccounts )
*  [SoftLayer_Network_LoadBalancer_Global_Account::getObject](/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/getObject )





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
[allowedNumberOfHosts]: #allowednumberofhosts
#### [allowedNumberOfHosts]
The maximum number of hosts that a global load balancer account is allowed to have.  
<span class="type-label">Type: </span>**integer**

-----
[averageConnectionsPerSecond]: #averageconnectionspersecond
#### [averageConnectionsPerSecond]
The average amount of connections per second used within the current billing cycle.  This number is updated daily.  
<span class="type-label">Type: </span>**float**

-----
[connectionsPerSecond]: #connectionspersecond
#### [connectionsPerSecond]
The amount of connections per second a global load balancer account may use within a billing cycle without being billed for an overage.  
<span class="type-label">Type: </span>**integer**

-----
[fallbackIp]: #fallbackip
#### [fallbackIp]
The IP address that will be return to a DNS request when none of the hosts for a global load balancer account could be returned.  
<span class="type-label">Type: </span>**string**

-----
[hostname]: #hostname
#### [hostname]
The hostname of a global load balancer account that is being load balanced.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
The unique identifier of a global load balancer account.  
<span class="type-label">Type: </span>**integer**

-----
[loadBalanceTypeId]: #loadbalancetypeid
#### [loadBalanceTypeId]
The identifier of the load balance method for a global load balancer account.  
<span class="type-label">Type: </span>**integer**

-----
[notes]: #notes
#### [notes]
Additional customer defined information for a global load balancer account.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
Your SoftLayer customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
The current billing item for a Global Load Balancer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[hosts]: #hosts
#### [hosts]
The hosts in the load balancing pool for a global load balancer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Host'>SoftLayer_Network_LoadBalancer_Global_Host[] </a>**

-----
[loadBalanceType]: #loadbalancetype
#### [loadBalanceType]
The load balance method of a global load balancer account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Type'>SoftLayer_Network_LoadBalancer_Global_Type </a>**

-----
[managedResourceFlag]: #managedresourceflag
#### [managedResourceFlag]
A flag indicating that the global load balancer is a managed resource.  
<span class="type-label">Type: </span>**boolean**


## Count

-----
[hostCount]: #hostcount
#### [hostCount]
A count of the hosts in the load balancing pool for a global load balancer account.   
<span class="type-label">Type: </span>**unsigned long**

</div>



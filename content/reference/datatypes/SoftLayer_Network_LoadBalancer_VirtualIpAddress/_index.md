---
title: "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
description: "The SoftLayer_Network_LoadBalancer_VirtualIpAddress data type contains all the information relating to a specific load b... "
layout: "datatype"
tags:
    - "datatype"
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
The SoftLayer_Network_LoadBalancer_VirtualIpAddress data type contains all the information relating to a specific load balancer assigned to a customer account. 

Information retained on the object itself is the virtual IP address, load balancing method, and any notes that are related to the load balancer.  There is also an array of SoftLayer_Network_LoadBalancer_Service objects, which represent the load balancer services, explained more fully in the SoftLayer_Network_LoadBalancer_Service documentation. 


### associatedMethods

*  [SoftLayer_Network_LoadBalancer_VirtualIpAddress::getObject](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getObject )





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
[connectionLimit]: #connectionlimit
#### [connectionLimit]
Connection limit on this VIP.  Can be upgraded through the upgradeConnectionLimit() function  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique ID for this object, used for the getObject method, and must be set if you are editing this object.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[loadBalancingMethod]: #loadbalancingmethod
#### [loadBalancingMethod]
The load balancing method that determines which server is used "next" by the load balancer.  The method is stored in an abbreviated form, represented in parentheses after the full name. Methods include: Round Robin (Value "rr"):  Each server is used sequentially in a circular queue Shortest Response (Value "sr"):  The server with the lowest ping at the last health check gets the next request Least Connections (Value "lc"):  The server with the least current connections is given the next request Persistent IP - Round Robin (Value "pi"): The same server will be returned to a request during a users session.  Servers are chosen through round robin. Persistent IP - Shortest Response (Value "pi-sr"): The same server will be returned to a request during a users session.  Servers are chosen through shortest response. Persistent IP - Least Connections (Value "pi-lc"): The same server will be returned to a request during a users session.  Servers are chosen through least connections. Insert Cookie - Round Robin (Value "ic"):  Inserts a cookie into the HTTP stream that will tie that client to a particular balanced server. Servers are chosen through round robin. Insert Cookie - Shortest Response (Value "ic-sr"): Inserts a cookie into the HTTP stream that will tie that client to a particular balanced server. Servers are chosen through shortest response. Insert Cookie - Least Connections (Value "ic-lc"): Inserts a cookie into the HTTP stream that will tie that client to a particular balanced server. Servers are chosen through least connections.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[loadBalancingMethodFullName]: #loadbalancingmethodfullname
#### [loadBalancingMethodFullName]
A human readable version of loadBalancingMethod, intended mainly for API users.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Date this load balancer was last modified  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name of the load balancer instance  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
User-created notes on this load balancer.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[securityCertificateId]: #securitycertificateid
#### [securityCertificateId]
The unique identifier of the Security Certificate to be utilized when SSL support is enabled.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[sourcePort]: #sourceport
#### [sourcePort]
This is the port for incoming traffic.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The connection type of this VIP.  Valid values are HTTP, FTP, TCP, UDP, and DNS.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[virtualIpAddress]: #virtualipaddress
#### [virtualIpAddress]
The virtual, public-facing IP address for your load balancer.  This is the address of all incoming traffic  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account that owns this load balancer.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The current billing item for the Load Balancer.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[customerManagedFlag]: #customermanagedflag
#### [customerManagedFlag]
If false, this VIP and associated services may be edited via the portal or the API. If true, you must configure this VIP manually on the device.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[managedResourceFlag]: #managedresourceflag
#### [managedResourceFlag]
A flag indicating that the load balancer is a managed resource.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[services]: #services
#### [services]
the services on this load balancer.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Service'>SoftLayer_Network_LoadBalancer_Service[] </a>**


</div>

## Count
<div class="prop-row">

-----
[serviceCount]: #servicecount
#### [serviceCount]
A count of the services on this load balancer.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>



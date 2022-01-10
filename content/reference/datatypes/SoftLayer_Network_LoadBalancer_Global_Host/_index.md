---
title: "SoftLayer_Network_LoadBalancer_Global_Host"
description: "The global load balancer service has been deprecated and is no longer available."
layout: "datatype"
tags:
    - "datatype"
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


### associatedMethods

*  [SoftLayer_Network_LoadBalancer_Global_Account::editObject](/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/editObject )
*  [SoftLayer_Network_LoadBalancer_Global_Host::getObject](/reference/services/SoftLayer_Network_LoadBalancer_Global_Host/getObject )





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
[destinationIp]: #destinationip
#### [destinationIp]
The IP address of the host that will be returned by the global load balancers in response to a dns request.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[destinationPort]: #destinationport
#### [destinationPort]
The port of the host that will be used for health checks.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[enabled]: #enabled
#### [enabled]
Whether the host is enabled or not.  The value can be '0' for disabled, or '1' for enabled.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[healthCheck]: #healthcheck
#### [healthCheck]
The health check type of a host.  Valid values include 'none', 'http', and 'tcp'.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[hits]: #hits
#### [hits]
The number of times the host was selected by the load balance method.  
<span class="type-label">Type: </span>**float**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique identifier of a global load balancer host.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[loadBalanceOrder]: #loadbalanceorder
#### [loadBalanceOrder]
The order of this host within the load balance pool.  This is only significant if the load balance method is set to failover.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
The location of a host in a datacenter.serverRoom format.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The health status of a host.  The status can be either 'UP', 'DOWN', or null which could mean that the health check type is set to 'none' or an update to the ip, port, or health check type was recently done and the host is waiting for the new status.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[weight]: #weight
#### [weight]
The load balance weight of a host.  The total weight of all hosts in the load balancing pool must not exceed 100.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[loadBalancerAccount]: #loadbalanceraccount
#### [loadBalancerAccount]
The global load balancer account a host belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Account'>SoftLayer_Network_LoadBalancer_Global_Account </a>**  



</div>

## Count
</div>



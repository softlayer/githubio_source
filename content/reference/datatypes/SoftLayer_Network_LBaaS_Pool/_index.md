---
title: "SoftLayer_Network_LBaaS_Pool"
description: "The SoftLayer_Network_LBaaS_Pool type presents a structure containing attributes of a load balancer pool such as the pro... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_Pool"
---

# SoftLayer_Network_LBaaS_Pool
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_Pool' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_LBaaS_Pool type presents a structure containing attributes of a load balancer pool such as the protocol, protocol port and the load balancing algorithm used. 



### seeAlso

* [SoftLayer_Network_LBaaS_Listener](/reference/datatypes/SoftLayer_Network_LBaaS_Listener )




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
[createDate]: #createdate
#### [createDate]
Create date of the pool instance  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[loadBalancingAlgorithm]: #loadbalancingalgorithm
#### [loadBalancingAlgorithm]
Load balancing algorithm: "ROUNDROBIN", "WEIGHTED_RR", "LEASTCONNECTION"  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Last updated date of the pool  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[protocol]: #protocol
#### [protocol]
Backends protocol, supported protocols are "TCP", "HTTP" and "HTTPS"  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[protocolPort]: #protocolport
#### [protocolPort]
Backends protocol port  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[provisioningStatus]: #provisioningstatus
#### [provisioningStatus]
Provisioning status of a load balancer pool.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[uuid]: #uuid
#### [uuid]
Instance uuid of the pool  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[healthMonitor]: #healthmonitor
#### [healthMonitor]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_HealthMonitor'>SoftLayer_Network_LBaaS_HealthMonitor </a>**


</div>
<div class="prop-row">

-----
[members]: #members
#### [members]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_Member'>SoftLayer_Network_LBaaS_Member[] </a>**


</div>
<div class="prop-row">

-----
[sessionAffinity]: #sessionaffinity
#### [sessionAffinity]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_SessionAffinity'>SoftLayer_Network_LBaaS_SessionAffinity </a>**


</div>

## Count
<div class="prop-row">

-----
[memberCount]: #membercount
#### [memberCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>



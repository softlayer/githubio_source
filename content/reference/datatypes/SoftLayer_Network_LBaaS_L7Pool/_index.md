---
title: "SoftLayer_Network_LBaaS_L7Pool"
description: "The SoftLayer_Network_LBaaS_L7Pool type presents a structure containing attributes of a load balancer's L7 pool such as... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Pool"
---

# SoftLayer_Network_LBaaS_L7Pool
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_L7Pool' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Pool' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_LBaaS_L7Pool type presents a structure containing attributes of a load balancer's L7 pool such as the protocol, and the load balancing algorithm used. L7 pool is used for redirect_pool action of the L7 policy and is different from the default pool 



### seeAlso

* [SoftLayer_Network_LBaaS_L7Pool](/reference/services/SoftLayer_Network_LBaaS_L7Pool )




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
Create date of the L7 pool instance  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**  



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
Last updated date of the L7 pool  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Name of the L7 pool.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[protocol]: #protocol
#### [protocol]
Backends protocol, supported protocol is, "HTTP"  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[provisioningStatus]: #provisioningstatus
#### [provisioningStatus]
Provisioning status of a load balancer's L7 pool.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[uuid]: #uuid
#### [uuid]
Instance uuid of the L7 pool  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[l7HealthMonitor]: #l7healthmonitor
#### [l7HealthMonitor]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7HealthMonitor'>SoftLayer_Network_LBaaS_L7HealthMonitor </a>**  



</div>
<div class="prop-row">

-----
[l7Members]: #l7members
#### [l7Members]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Member'>SoftLayer_Network_LBaaS_L7Member[] </a>**  



</div>
<div class="prop-row">

-----
[l7Policies]: #l7policies
#### [l7Policies]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Policy'>SoftLayer_Network_LBaaS_L7Policy[] </a>**  



</div>
<div class="prop-row">

-----
[l7SessionAffinity]: #l7sessionaffinity
#### [l7SessionAffinity]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7SessionAffinity'>SoftLayer_Network_LBaaS_L7SessionAffinity </a>**  



</div>

## Count
<div class="prop-row">

-----
[l7MemberCount]: #l7membercount
#### [l7MemberCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[l7PolicyCount]: #l7policycount
#### [l7PolicyCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>



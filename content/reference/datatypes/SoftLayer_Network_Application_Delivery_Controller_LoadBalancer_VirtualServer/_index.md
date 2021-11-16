---
title: "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer"
---

# SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer' >Datatype</a></li>
    </ul>
</div>

## Description 








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
[allocation]: #allocation
#### [allocation]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[port]: #port
#### [port]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[routingMethodId]: #routingmethodid
#### [routingMethodId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[virtualIpAddressId]: #virtualipaddressid
#### [virtualIpAddressId]
  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[routingMethod]: #routingmethod
#### [routingMethod]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method </a>**  



</div>
<div class="prop-row">

-----
[scaleLoadBalancers]: #scaleloadbalancers
#### [scaleLoadBalancers]
Collection of scale load balancers this virtual server applies to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_LoadBalancer'>SoftLayer_Scale_LoadBalancer[] </a>**  



</div>
<div class="prop-row">

-----
[serviceGroups]: #servicegroups
#### [serviceGroups]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group[] </a>**  



</div>
<div class="prop-row">

-----
[virtualIpAddress]: #virtualipaddress
#### [virtualIpAddress]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress </a>**  



</div>

## Count
<div class="prop-row">

-----
[scaleLoadBalancerCount]: #scaleloadbalancercount
#### [scaleLoadBalancerCount]
A count of collection of scale load balancers this virtual server applies to.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[serviceGroupCount]: #servicegroupcount
#### [serviceGroupCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>



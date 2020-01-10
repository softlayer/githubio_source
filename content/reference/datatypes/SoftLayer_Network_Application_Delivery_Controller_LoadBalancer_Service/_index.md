---
title: "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service"
---

# SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service' >Datatype</a></li>
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
[enabled]: #enabled
#### [enabled]
  
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
[ipAddressId]: #ipaddressid
#### [ipAddressId]
  
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
[status]: #status
#### [status]
  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[groupReferences]: #groupreferences
#### [groupReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference[] </a>**


</div>
<div class="prop-row">

-----
[groups]: #groups
#### [groups]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group[] </a>**


</div>
<div class="prop-row">

-----
[healthCheck]: #healthcheck
#### [healthCheck]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check </a>**


</div>
<div class="prop-row">

-----
[healthChecks]: #healthchecks
#### [healthChecks]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check[] </a>**


</div>
<div class="prop-row">

-----
[ipAddress]: #ipaddress
#### [ipAddress]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[serviceGroup]: #servicegroup
#### [serviceGroup]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group </a>**


</div>

## Count
<div class="prop-row">

-----
[groupCount]: #groupcount
#### [groupCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[groupReferenceCount]: #groupreferencecount
#### [groupReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[healthCheckCount]: #healthcheckcount
#### [healthCheckCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>



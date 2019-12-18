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
[enabled]: #enabled
#### [enabled]
  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[ipAddressId]: #ipaddressid
#### [ipAddressId]
  
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
  
<span class="type-label">Type: </span>**string**

-----
[notes]: #notes
#### [notes]
  
<span class="type-label">Type: </span>**string**

-----
[port]: #port
#### [port]
  
<span class="type-label">Type: </span>**integer**

-----
[status]: #status
#### [status]
  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[groupReferences]: #groupreferences
#### [groupReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference[] </a>**

-----
[groups]: #groups
#### [groups]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group[] </a>**

-----
[healthCheck]: #healthcheck
#### [healthCheck]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check </a>**

-----
[healthChecks]: #healthchecks
#### [healthChecks]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check[] </a>**

-----
[ipAddress]: #ipaddress
#### [ipAddress]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**

-----
[serviceGroup]: #servicegroup
#### [serviceGroup]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group </a>**


## Count

-----
[groupCount]: #groupcount
#### [groupCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[groupReferenceCount]: #groupreferencecount
#### [groupReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[healthCheckCount]: #healthcheckcount
#### [healthCheckCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>



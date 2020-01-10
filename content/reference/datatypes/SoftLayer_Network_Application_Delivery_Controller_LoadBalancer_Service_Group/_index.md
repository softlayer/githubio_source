---
title: "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group"
---

# SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group' >Datatype</a></li>
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
[routingMethodId]: #routingmethodid
#### [routingMethodId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[routingTypeId]: #routingtypeid
#### [routingTypeId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[timeout]: #timeout
#### [timeout]
The timeout value for connections from remote clients to the load balancer. Timeout values are only valid for HTTP service groups.   
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
[routingType]: #routingtype
#### [routingType]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type </a>**


</div>
<div class="prop-row">

-----
[serviceReferences]: #servicereferences
#### [serviceReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference[] </a>**


</div>
<div class="prop-row">

-----
[services]: #services
#### [services]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service[] </a>**


</div>
<div class="prop-row">

-----
[virtualServer]: #virtualserver
#### [virtualServer]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer </a>**


</div>
<div class="prop-row">

-----
[virtualServers]: #virtualservers
#### [virtualServers]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer[] </a>**


</div>

## Count
<div class="prop-row">

-----
[serviceCount]: #servicecount
#### [serviceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[serviceReferenceCount]: #servicereferencecount
#### [serviceReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualServerCount]: #virtualservercount
#### [virtualServerCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>



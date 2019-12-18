---
title: "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check"
---

# SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check' >Datatype</a></li>
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
[healthCheckTypeId]: #healthchecktypeid
#### [healthCheckTypeId]
  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
  
<span class="type-label">Type: </span>**string**

-----
[notes]: #notes
#### [notes]
  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[attributes]: #attributes
#### [attributes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute[] </a>**

-----
[scaleLoadBalancers]: #scaleloadbalancers
#### [scaleLoadBalancers]
Collection of scale load balancers that use this health check.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_LoadBalancer'>SoftLayer_Scale_LoadBalancer[] </a>**

-----
[services]: #services
#### [services]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service[] </a>**

-----
[type]: #type
#### [type]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check_Type'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check_Type </a>**


## Count

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[scaleLoadBalancerCount]: #scaleloadbalancercount
#### [scaleLoadBalancerCount]
A count of collection of scale load balancers that use this health check.   
<span class="type-label">Type: </span>**unsigned long**


-----
[serviceCount]: #servicecount
#### [serviceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>



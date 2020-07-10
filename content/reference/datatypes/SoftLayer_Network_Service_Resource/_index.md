---
title: "SoftLayer_Network_Service_Resource"
description: "The SoftLayer_Network_Service_Resource is used to store information related to a service.  It is used for determining th... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Service_Resource"
---

# SoftLayer_Network_Service_Resource
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Service_Resource' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Service_Resource is used to store information related to a service.  It is used for determining the correct resource to connect to for a given service, like NAS, Evault, etc. 





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
[backendIpAddress]: #backendipaddress
#### [backendIpAddress]
The backend IP address for this resource   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[frontendIpAddress]: #frontendipaddress
#### [frontendIpAddress]
The frontend IP address for this resource   
<span class="type-label">Type: </span>**string**


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
The name associated with this resource   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[apiHost]: #apihost
#### [apiHost]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[apiPassword]: #apipassword
#### [apiPassword]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[apiPath]: #apipath
#### [apiPath]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[apiPort]: #apiport
#### [apiPort]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[apiProtocol]: #apiprotocol
#### [apiProtocol]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[apiUsername]: #apiusername
#### [apiUsername]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[apiVersion]: #apiversion
#### [apiVersion]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Service_Resource_Attribute'>SoftLayer_Network_Service_Resource_Attribute[] </a>**


</div>
<div class="prop-row">

-----
[datacenter]: #datacenter
#### [datacenter]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[netappVolumeName]: #netappvolumename
#### [netappVolumeName]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[networkDevice]: #networkdevice
#### [networkDevice]
The hardware information associated with this resource.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[sshUsername]: #sshusername
#### [sshUsername]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The network information associated with this resource.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Service_Resource_Type'>SoftLayer_Network_Service_Resource_Type </a>**


</div>

## Count
<div class="prop-row">

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>



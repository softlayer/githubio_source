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
[backendIpAddress]: #backendipaddress
#### [backendIpAddress]
The backend IP address for this resource   
<span class="type-label">Type: </span>**string**

-----
[frontendIpAddress]: #frontendipaddress
#### [frontendIpAddress]
The frontend IP address for this resource   
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
The name associated with this resource   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[apiHost]: #apihost
#### [apiHost]
  
<span class="type-label">Type: </span>**string**

-----
[apiPassword]: #apipassword
#### [apiPassword]
  
<span class="type-label">Type: </span>**string**

-----
[apiPath]: #apipath
#### [apiPath]
  
<span class="type-label">Type: </span>**string**

-----
[apiPort]: #apiport
#### [apiPort]
  
<span class="type-label">Type: </span>**string**

-----
[apiProtocol]: #apiprotocol
#### [apiProtocol]
  
<span class="type-label">Type: </span>**string**

-----
[apiUsername]: #apiusername
#### [apiUsername]
  
<span class="type-label">Type: </span>**string**

-----
[apiVersion]: #apiversion
#### [apiVersion]
  
<span class="type-label">Type: </span>**string**

-----
[attributes]: #attributes
#### [attributes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Service_Resource_Attribute'>SoftLayer_Network_Service_Resource_Attribute[] </a>**

-----
[datacenter]: #datacenter
#### [datacenter]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[networkDevice]: #networkdevice
#### [networkDevice]
The hardware information associated with this resource.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[sshUsername]: #sshusername
#### [sshUsername]
  
<span class="type-label">Type: </span>**string**

-----
[type]: #type
#### [type]
The network information associated with this resource.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Service_Resource_Type'>SoftLayer_Network_Service_Resource_Type </a>**


## Count

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>



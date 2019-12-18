---
title: "SoftLayer_Network_Subnet_Registration_Event"
description: "Each time a [SoftLayer_Network_Subnet_Registration]({{<ref 'reference/datatypes/SoftLayer_Network_Subnet_Registration'>}... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration_Event"
---

# SoftLayer_Network_Subnet_Registration_Event
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Event' >Datatype</a></li>
    </ul>
</div>

## Description 
Each time a [SoftLayer_Network_Subnet_Registration]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration">}}) object is created or modified, the system will generate an event for it. Additional actions that would create an event include RIR responses and error cases. * 





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
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
Unique numeric ID of the event object   
<span class="type-label">Type: </span>**integer**

-----
[message]: #message
#### [message]
A string message indicating what took place during this event   
<span class="type-label">Type: </span>**string**

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[registrationId]: #registrationid
#### [registrationId]
The numeric ID of the related [SoftLayer_Network_Subnet_Registration]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration">}}) object   
<span class="type-label">Type: </span>**integer**

-----
[typeId]: #typeid
#### [typeId]
The numeric ID of the associated [SoftLayer_Network_Subnet_Registration_Event_Type]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration_Event_Type">}}) object   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[registration]: #registration
#### [registration]
The registration this event pertains to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration'>SoftLayer_Network_Subnet_Registration </a>**

-----
[type]: #type
#### [type]
The type of this event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Event_Type'>SoftLayer_Network_Subnet_Registration_Event_Type </a>**


## Count
</div>



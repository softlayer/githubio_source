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
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique numeric ID of the event object   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[message]: #message
#### [message]
A string message indicating what took place during this event   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[registrationId]: #registrationid
#### [registrationId]
The numeric ID of the related [SoftLayer_Network_Subnet_Registration]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration">}}) object   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
The numeric ID of the associated [SoftLayer_Network_Subnet_Registration_Event_Type]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration_Event_Type">}}) object   
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[registration]: #registration
#### [registration]
The registration this event pertains to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration'>SoftLayer_Network_Subnet_Registration </a>**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of this event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Event_Type'>SoftLayer_Network_Subnet_Registration_Event_Type </a>**  



</div>

## Count
</div>



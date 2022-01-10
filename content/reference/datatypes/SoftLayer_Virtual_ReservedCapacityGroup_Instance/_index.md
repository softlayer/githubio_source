---
title: "SoftLayer_Virtual_ReservedCapacityGroup_Instance"
description: "This data type presents the structure for a virtual reserved capacity group instance."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_ReservedCapacityGroup_Instance"
---

# SoftLayer_Virtual_ReservedCapacityGroup_Instance
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_ReservedCapacityGroup_Instance' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_ReservedCapacityGroup_Instance' >Datatype</a></li>
    </ul>
</div>

## Description 


This data type presents the structure for a virtual reserved capacity group instance. 





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
The date that the reserved capacity group instance was created.   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[guestId]: #guestid
#### [guestId]
The virtual guest ID associated with this reserved capacity group instance.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The reserved capacity group instance's associated unique ID.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date that the reserved capacity group instance was last modified.   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[reservedCapacityGroupId]: #reservedcapacitygroupid
#### [reservedCapacityGroupId]
The ID of the reserved capacity group this instance is associated with.   
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[availableFlag]: #availableflag
#### [availableFlag]
Flag to indecate whether or not the reserved instance is available or not.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for the reserved capacity group instance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**  



</div>
<div class="prop-row">

-----
[guest]: #guest
#### [guest]
The virtual guest associated with this reserved capacity group instance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**  



</div>
<div class="prop-row">

-----
[reservedCapacityGroup]: #reservedcapacitygroup
#### [reservedCapacityGroup]
The reserved instances that are members of this reserved capacity group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_ReservedCapacityGroup'>SoftLayer_Virtual_ReservedCapacityGroup </a>**  



</div>

## Count
</div>



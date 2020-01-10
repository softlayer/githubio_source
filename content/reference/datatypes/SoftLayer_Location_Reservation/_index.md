---
title: "SoftLayer_Location_Reservation"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Reservation"
---

# SoftLayer_Location_Reservation
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Location_Reservation' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Reservation' >Datatype</a></li>
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
[allotmentId]: #allotmentid
#### [allotmentId]
  
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
[locationId]: #locationid
#### [locationId]
  
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
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account that a billing item belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[allotment]: #allotment
#### [allotment]
The bandwidth allotment that the reservation belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>**


</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The bandwidth allotment that the reservation belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
The datacenter location that the reservation belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[locationReservationRack]: #locationreservationrack
#### [locationReservationRack]
Rack information for the reservation  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Reservation_Rack'>SoftLayer_Location_Reservation_Rack </a>**


</div>

## Count
</div>



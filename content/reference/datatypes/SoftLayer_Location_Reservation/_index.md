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
[allotmentId]: #allotmentid
#### [allotmentId]
  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[locationId]: #locationid
#### [locationId]
  
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
[account]: #account
#### [account]
The account that a billing item belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[allotment]: #allotment
#### [allotment]
The bandwidth allotment that the reservation belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
The bandwidth allotment that the reservation belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[location]: #location
#### [location]
The datacenter location that the reservation belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[locationReservationRack]: #locationreservationrack
#### [locationReservationRack]
Rack information for the reservation  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Reservation_Rack'>SoftLayer_Location_Reservation_Rack </a>**


## Count
</div>



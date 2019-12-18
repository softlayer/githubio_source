---
title: "SoftLayer_Location_Reservation_Rack"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Reservation_Rack"
---

# SoftLayer_Location_Reservation_Rack
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Location_Reservation_Rack' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Reservation_Rack' >Datatype</a></li>
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
[locationId]: #locationid
#### [locationId]
  
<span class="type-label">Type: </span>**integer**

-----
[locationReservationId]: #locationreservationid
#### [locationReservationId]
  
<span class="type-label">Type: </span>**integer**

-----
[networkConnectionCapacity]: #networkconnectioncapacity
#### [networkConnectionCapacity]
  
<span class="type-label">Type: </span>**integer**

-----
[networkConnectionReservation]: #networkconnectionreservation
#### [networkConnectionReservation]
  
<span class="type-label">Type: </span>**integer**

-----
[powerConnectionCapacity]: #powerconnectioncapacity
#### [powerConnectionCapacity]
  
<span class="type-label">Type: </span>**integer**

-----
[powerConnectionReservation]: #powerconnectionreservation
#### [powerConnectionReservation]
  
<span class="type-label">Type: </span>**integer**

-----
[slotCapacity]: #slotcapacity
#### [slotCapacity]
  
<span class="type-label">Type: </span>**integer**

-----
[slotReservation]: #slotreservation
#### [slotReservation]
  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[allotment]: #allotment
#### [allotment]
The bandwidth allotment that the reservation belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>**

-----
[children]: #children
#### [children]
Members of the rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Reservation_Rack_Member'>SoftLayer_Location_Reservation_Rack_Member[] </a>**

-----
[location]: #location
#### [location]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[locationReservation]: #locationreservation
#### [locationReservation]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Reservation'>SoftLayer_Location_Reservation </a>**


## Count

-----
[childrenCount]: #childrencount
#### [childrenCount]
A count of members of the rack.   
<span class="type-label">Type: </span>**unsigned long**

</div>



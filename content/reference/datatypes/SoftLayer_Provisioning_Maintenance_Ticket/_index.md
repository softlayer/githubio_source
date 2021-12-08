---
title: "SoftLayer_Provisioning_Maintenance_Ticket"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Provisioning"
classes:
    - "SoftLayer_Provisioning_Maintenance_Ticket"
---

# SoftLayer_Provisioning_Maintenance_Ticket
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Provisioning_Maintenance_Ticket' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Provisioning_Maintenance_Ticket' >Datatype</a></li>
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
[maintClassId]: #maintclassid
#### [maintClassId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[maintWindowId]: #maintwindowid
#### [maintWindowId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[maintenanceDate]: #maintenancedate
#### [maintenanceDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[ticketId]: #ticketid
#### [ticketId]
  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[availableSlots]: #availableslots
#### [availableSlots]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Maintenance_Slots'>SoftLayer_Provisioning_Maintenance_Slots </a>**  



</div>
<div class="prop-row">

-----
[maintenanceClass]: #maintenanceclass
#### [maintenanceClass]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Maintenance_Classification'>SoftLayer_Provisioning_Maintenance_Classification </a>**  



</div>
<div class="prop-row">

-----
[ticket]: #ticket
#### [ticket]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**  



</div>

## Count
</div>



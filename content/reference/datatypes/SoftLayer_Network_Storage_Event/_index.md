---
title: "SoftLayer_Network_Storage_Event"
description: "Storage volumes can create various events to keep track of what has occurred to the volume. Events provide an audit trai... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Event"
---

# SoftLayer_Network_Storage_Event
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Event' >Datatype</a></li>
    </ul>
</div>

## Description 


Storage volumes can create various events to keep track of what has occurred to the volume. Events provide an audit trail that can be used to verify that various tasks have occurred, such as snapshots to be created by a schedule or remote replication synchronization. 





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
The date an event was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[message]: #message
#### [message]
The message text for an event.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[scheduleId]: #scheduleid
#### [scheduleId]
An identifier for the schedule which is associated with an event.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
An identifier for the type of an event.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[volumeId]: #volumeid
#### [volumeId]
The volume id which an event is associated with.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[schedule]: #schedule
#### [schedule]
A schedule that is associated with an event. Not all events will have a schedule.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule'>SoftLayer_Network_Storage_Schedule </a>**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
A Storage volume's event type. The type provides a standardized definition for an event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Event_Type'>SoftLayer_Network_Storage_Event_Type </a>**  



</div>
<div class="prop-row">

-----
[volume]: #volume
#### [volume]
The associated volume for an event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**  



</div>

## Count
</div>



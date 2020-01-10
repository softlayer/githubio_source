---
title: "SoftLayer_Network_Storage_Schedule"
description: "Schedules can be created for select Storage services, such as iscsi. These schedules are used to perform various tasks s... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Schedule"
---

# SoftLayer_Network_Storage_Schedule
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Storage_Schedule' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule' >Datatype</a></li>
    </ul>
</div>

## Description 
Schedules can be created for select Storage services, such as iscsi. These schedules are used to perform various tasks such as scheduling snapshots or synchronizing replicants. 





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
[active]: #active
#### [active]
A flag which determines if a schedule is active.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date a schedule was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A schedule's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a schedule was last modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A schedule's name, for example 'Daily'.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[partnershipId]: #partnershipid
#### [partnershipId]
The partnership id which a schedule is associated with.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
The type id which a schedule is associated with.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[volumeId]: #volumeid
#### [volumeId]
The volume id which a schedule is associated with.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[day]: #day
#### [day]
The hour parameter of this schedule.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[dayOfMonth]: #dayofmonth
#### [dayOfMonth]
The day of the month parameter of this schedule.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[dayOfWeek]: #dayofweek
#### [dayOfWeek]
The day of the week parameter of this schedule.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[events]: #events
#### [events]
Events which have been created as the result of a schedule execution.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Event'>SoftLayer_Network_Storage_Event[] </a>**


</div>
<div class="prop-row">

-----
[hour]: #hour
#### [hour]
The hour parameter of this schedule.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[minute]: #minute
#### [minute]
The minute parameter of this schedule.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[monthOfYear]: #monthofyear
#### [monthOfYear]
The month of the year parameter of this schedule.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[partnership]: #partnership
#### [partnership]
The associated partnership for a schedule.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Partnership'>SoftLayer_Network_Storage_Partnership </a>**


</div>
<div class="prop-row">

-----
[properties]: #properties
#### [properties]
Properties used for configuration of a schedule.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule_Property'>SoftLayer_Network_Storage_Schedule_Property[] </a>**


</div>
<div class="prop-row">

-----
[replicaSnapshots]: #replicasnapshots
#### [replicaSnapshots]
Replica snapshots which have been created as the result of this schedule's execution.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[retentionCount]: #retentioncount
#### [retentionCount]
The number of snapshots this schedule is configured to retain.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[second]: #second
#### [second]
The minute parameter of this schedule.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[snapshots]: #snapshots
#### [snapshots]
Snapshots which have been created as the result of this schedule's execution.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type provides a standardized definition for a schedule.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule_Type'>SoftLayer_Network_Storage_Schedule_Type </a>**


</div>
<div class="prop-row">

-----
[volume]: #volume
#### [volume]
The associated volume for a schedule.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**


</div>

## Count
<div class="prop-row">

-----
[eventCount]: #eventcount
#### [eventCount]
A count of events which have been created as the result of a schedule execution.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[propertyCount]: #propertycount
#### [propertyCount]
A count of properties used for configuration of a schedule.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[replicaSnapshotCount]: #replicasnapshotcount
#### [replicaSnapshotCount]
A count of replica snapshots which have been created as the result of this schedule's execution.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[snapshotCount]: #snapshotcount
#### [snapshotCount]
A count of snapshots which have been created as the result of this schedule's execution.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>



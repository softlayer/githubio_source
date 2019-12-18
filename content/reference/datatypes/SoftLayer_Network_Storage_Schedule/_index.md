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
[active]: #active
#### [active]
A flag which determines if a schedule is active.  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The date a schedule was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
A schedule's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a schedule was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
A schedule's name, for example 'Daily'.  
<span class="type-label">Type: </span>**string**

-----
[partnershipId]: #partnershipid
#### [partnershipId]
The partnership id which a schedule is associated with.  
<span class="type-label">Type: </span>**integer**

-----
[typeId]: #typeid
#### [typeId]
The type id which a schedule is associated with.  
<span class="type-label">Type: </span>**integer**

-----
[volumeId]: #volumeid
#### [volumeId]
The volume id which a schedule is associated with.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[day]: #day
#### [day]
The hour parameter of this schedule.  
<span class="type-label">Type: </span>**string**

-----
[dayOfMonth]: #dayofmonth
#### [dayOfMonth]
The day of the month parameter of this schedule.  
<span class="type-label">Type: </span>**string**

-----
[dayOfWeek]: #dayofweek
#### [dayOfWeek]
The day of the week parameter of this schedule.  
<span class="type-label">Type: </span>**string**

-----
[events]: #events
#### [events]
Events which have been created as the result of a schedule execution.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Event'>SoftLayer_Network_Storage_Event[] </a>**

-----
[hour]: #hour
#### [hour]
The hour parameter of this schedule.  
<span class="type-label">Type: </span>**string**

-----
[minute]: #minute
#### [minute]
The minute parameter of this schedule.  
<span class="type-label">Type: </span>**string**

-----
[monthOfYear]: #monthofyear
#### [monthOfYear]
The month of the year parameter of this schedule.  
<span class="type-label">Type: </span>**string**

-----
[partnership]: #partnership
#### [partnership]
The associated partnership for a schedule.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Partnership'>SoftLayer_Network_Storage_Partnership </a>**

-----
[properties]: #properties
#### [properties]
Properties used for configuration of a schedule.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule_Property'>SoftLayer_Network_Storage_Schedule_Property[] </a>**

-----
[replicaSnapshots]: #replicasnapshots
#### [replicaSnapshots]
Replica snapshots which have been created as the result of this schedule's execution.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[retentionCount]: #retentioncount
#### [retentionCount]
The number of snapshots this schedule is configured to retain.  
<span class="type-label">Type: </span>**string**

-----
[second]: #second
#### [second]
The minute parameter of this schedule.  
<span class="type-label">Type: </span>**string**

-----
[snapshots]: #snapshots
#### [snapshots]
Snapshots which have been created as the result of this schedule's execution.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[type]: #type
#### [type]
The type provides a standardized definition for a schedule.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Schedule_Type'>SoftLayer_Network_Storage_Schedule_Type </a>**

-----
[volume]: #volume
#### [volume]
The associated volume for a schedule.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**


## Count

-----
[eventCount]: #eventcount
#### [eventCount]
A count of events which have been created as the result of a schedule execution.   
<span class="type-label">Type: </span>**unsigned long**


-----
[propertyCount]: #propertycount
#### [propertyCount]
A count of properties used for configuration of a schedule.   
<span class="type-label">Type: </span>**unsigned long**


-----
[replicaSnapshotCount]: #replicasnapshotcount
#### [replicaSnapshotCount]
A count of replica snapshots which have been created as the result of this schedule's execution.   
<span class="type-label">Type: </span>**unsigned long**


-----
[snapshotCount]: #snapshotcount
#### [snapshotCount]
A count of snapshots which have been created as the result of this schedule's execution.   
<span class="type-label">Type: </span>**unsigned long**

</div>



---
title: "SoftLayer_Network_Storage_Schedule"
description: "Schedules can be created for select Storage services, such as iscsi. These schedules are used to perform various tasks s... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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

The schedule service can be used to create, edit, or delete a schedule. Schedules are defined by the properties associated with them to specify values such as the start date, interval, or end date of the schedule. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_Network_Storage_Schedule/createObject)
Create a nas volume schedule

</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_Network_Storage_Schedule/deleteObject)
Delete a network storage schedule

</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_Storage_Schedule/editObject)
Edit a nas volume schedule

</div>

<div class="method-row">

#### [getDay](/reference/services/SoftLayer_Network_Storage_Schedule/getDay)
Retrieve the hour parameter of this schedule.

</div>

<div class="method-row">

#### [getDayOfMonth](/reference/services/SoftLayer_Network_Storage_Schedule/getDayOfMonth)
Retrieve the day of the month parameter of this schedule.

</div>

<div class="method-row">

#### [getDayOfWeek](/reference/services/SoftLayer_Network_Storage_Schedule/getDayOfWeek)
Retrieve the day of the week parameter of this schedule.

</div>

<div class="method-row">

#### [getEvents](/reference/services/SoftLayer_Network_Storage_Schedule/getEvents)
Retrieve events which have been created as the result of a schedule execution.

</div>

<div class="method-row">

#### [getHour](/reference/services/SoftLayer_Network_Storage_Schedule/getHour)
Retrieve the hour parameter of this schedule.

</div>

<div class="method-row">

#### [getMinute](/reference/services/SoftLayer_Network_Storage_Schedule/getMinute)
Retrieve the minute parameter of this schedule.

</div>

<div class="method-row">

#### [getMonthOfYear](/reference/services/SoftLayer_Network_Storage_Schedule/getMonthOfYear)
Retrieve the month of the year parameter of this schedule.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Storage_Schedule/getObject)
Retrieve a SoftLayer_Network_Storage_Schedule record.

</div>

<div class="method-row">

#### [getPartnership](/reference/services/SoftLayer_Network_Storage_Schedule/getPartnership)
Retrieve the associated partnership for a schedule.

</div>

<div class="method-row">

#### [getProperties](/reference/services/SoftLayer_Network_Storage_Schedule/getProperties)
Retrieve properties used for configuration of a schedule.

</div>

<div class="method-row">

#### [getReplicaSnapshots](/reference/services/SoftLayer_Network_Storage_Schedule/getReplicaSnapshots)
Retrieve replica snapshots which have been created as the result of this schedule's execution.

</div>

<div class="method-row">

#### [getRetentionCount](/reference/services/SoftLayer_Network_Storage_Schedule/getRetentionCount)
Retrieve the number of snapshots this schedule is configured to retain.

</div>

<div class="method-row">

#### [getSecond](/reference/services/SoftLayer_Network_Storage_Schedule/getSecond)
Retrieve the minute parameter of this schedule.

</div>

<div class="method-row">

#### [getSnapshots](/reference/services/SoftLayer_Network_Storage_Schedule/getSnapshots)
Retrieve snapshots which have been created as the result of this schedule's execution.

</div>

<div class="method-row">

#### [getType](/reference/services/SoftLayer_Network_Storage_Schedule/getType)
Retrieve the type provides a standardized definition for a schedule.

</div>

<div class="method-row">

#### [getVolume](/reference/services/SoftLayer_Network_Storage_Schedule/getVolume)
Retrieve the associated volume for a schedule.

</div>
</div>

</div>


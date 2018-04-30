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



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a nas volume schedule</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete a network storage schedule</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit a nas volume schedule</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getDay'> getDay</a> </span>
            <div class='views-field-body'>Retrieve the hour parameter of this schedule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getDayOfMonth'> getDayOfMonth</a> </span>
            <div class='views-field-body'>Retrieve the day of the month parameter of this schedule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getDayOfWeek'> getDayOfWeek</a> </span>
            <div class='views-field-body'>Retrieve the day of the week parameter of this schedule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getEvents'> getEvents</a> </span>
            <div class='views-field-body'>Retrieve events which have been created as the result of a schedule execution.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getHour'> getHour</a> </span>
            <div class='views-field-body'>Retrieve the hour parameter of this schedule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getMinute'> getMinute</a> </span>
            <div class='views-field-body'>Retrieve the minute parameter of this schedule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getMonthOfYear'> getMonthOfYear</a> </span>
            <div class='views-field-body'>Retrieve the month of the year parameter of this schedule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Storage_Schedule record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getPartnership'> getPartnership</a> </span>
            <div class='views-field-body'>Retrieve the associated partnership for a schedule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getProperties'> getProperties</a> </span>
            <div class='views-field-body'>Retrieve properties used for configuration of a schedule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getReplicaSnapshots'> getReplicaSnapshots</a> </span>
            <div class='views-field-body'>Retrieve replica snapshots which have been created as the result of this schedule's execution.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getRetentionCount'> getRetentionCount</a> </span>
            <div class='views-field-body'>Retrieve the number of snapshots this schedule is configured to retain.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getSecond'> getSecond</a> </span>
            <div class='views-field-body'>Retrieve the minute parameter of this schedule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getSnapshots'> getSnapshots</a> </span>
            <div class='views-field-body'>Retrieve snapshots which have been created as the result of this schedule's execution.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getType'> getType</a> </span>
            <div class='views-field-body'>Retrieve the type provides a standardized definition for a schedule.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_Schedule/getVolume'> getVolume</a> </span>
            <div class='views-field-body'>Retrieve the associated volume for a schedule.</div>
        </div>
        </div>
</div>


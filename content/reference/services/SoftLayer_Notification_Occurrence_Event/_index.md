---
title: "SoftLayer_Notification_Occurrence_Event"
description: "The [[SoftLayer_Notification_Occurrence_Event]] service represents all events with potential to cause a disruption in se... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Occurrence_Event"
---
# SoftLayer_Notification_Occurrence_Event
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Notification_Occurrence_Event' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event' >Datatype</a></li>
    </ul>
</div>

## Description
The [[SoftLayer_Notification_Occurrence_Event]] service represents all events with potential to cause a disruption in service. 
        
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/acknowledgeNotification'> acknowledgeNotification</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getAcknowledgedFlag'> getAcknowledgedFlag</a> </span>
            <div class='views-field-body'>Retrieve indicates whether or not this event has been acknowledged by the user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getAllObjects'> getAllObjects</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getAttachedFile'> getAttachedFile</a> </span>
            <div class='views-field-body'>Retrieve a file attached to an event.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getAttachments'> getAttachments</a> </span>
            <div class='views-field-body'>Retrieve a collection of attachments for this event which provide supplementary information to impacted users some examples are RFO (Reason For Outage) and root cause analysis documents.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getFirstUpdate'> getFirstUpdate</a> </span>
            <div class='views-field-body'>Retrieve the first update for this event.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getImpactedAccountCount'> getImpactedAccountCount</a> </span>
            <div class='views-field-body'>Get the number of impacted owned accounts for the current user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getImpactedAccounts'> getImpactedAccounts</a> </span>
            <div class='views-field-body'>Retrieve a collection of accounts impacted by this event. Each impacted account record relates directly to a [[SoftLayer_Account]].</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getImpactedDeviceCount'> getImpactedDeviceCount</a> </span>
            <div class='views-field-body'>Get the number of impacted devices.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getImpactedDevices'> getImpactedDevices</a> </span>
            <div class='views-field-body'>Get devices impacted by this event</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getImpactedResources'> getImpactedResources</a> </span>
            <div class='views-field-body'>Retrieve a collection of resources impacted by this event. Each record will relate to some physical resource that the user has access to such as [[SoftLayer_Hardware]] or [[SoftLayer_Virtual_Guest]].</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getImpactedUsers'> getImpactedUsers</a> </span>
            <div class='views-field-body'>Retrieve a collection of users impacted by this event. Each impacted user record relates directly to a [[SoftLayer_User_Customer]].</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getLastUpdate'> getLastUpdate</a> </span>
            <div class='views-field-body'>Retrieve the last update for this event.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getNotificationOccurrenceEventType'> getNotificationOccurrenceEventType</a> </span>
            <div class='views-field-body'>Retrieve the type of event such as planned or unplanned maintenance.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Notification_Occurrence_Event record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getStatusCode'> getStatusCode</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Notification_Occurrence_Event/getUpdates'> getUpdates</a> </span>
            <div class='views-field-body'>Retrieve all updates for this event.</div>
        </div>
        </div>
</div>


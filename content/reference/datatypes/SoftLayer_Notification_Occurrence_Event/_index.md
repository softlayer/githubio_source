---
title: "SoftLayer_Notification_Occurrence_Event"
description: ""
layout: "datatype"
tags:
    - "datatype"
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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#endDate" name=endDate>endDate</a>
            </span>
            <div class='views-field-body'>When this event will end. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>Unique identifier for this event. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#lastImpactedUserCount" name=lastImpactedUserCount>lastImpactedUserCount</a>
            </span>
            <div class='views-field-body'>Latest count of users impacted by this event. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>When this event was last updated. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recoveryTime" name=recoveryTime>recoveryTime</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#startDate" name=startDate>startDate</a>
            </span>
            <div class='views-field-body'>When this event started. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#subject" name=subject>subject</a>
            </span>
            <div class='views-field-body'>Brief description of this event. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#summary" name=summary>summary</a>
            </span>
            <div class='views-field-body'>Details of this event. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#systemTicketId" name=systemTicketId>systemTicketId</a>
            </span>
            <div class='views-field-body'>Unique identifier for the [[SoftLayer_Ticket]] associated with this event. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#acknowledgedFlag" name=acknowledgedFlag>acknowledgedFlag</a>
            </span>
            <div class='views-field-body'>Indicates whether or not this event has been acknowledged by the user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#attachments" name=attachments>attachments</a>
            </span>
            <div class='views-field-body'>A collection of attachments for this event which provide supplementary information to impacted users some examples are RFO (Reason For Outage) and root cause analysis documents. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event_Attachment'>SoftLayer_Notification_Occurrence_Event_Attachment[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#firstUpdate" name=firstUpdate>firstUpdate</a>
            </span>
            <div class='views-field-body'>The first update for this event. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Update'>SoftLayer_Notification_Occurrence_Update </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#impactedAccounts" name=impactedAccounts>impactedAccounts</a>
            </span>
            <div class='views-field-body'>A collection of accounts impacted by this event. Each impacted account record relates directly to a [[SoftLayer_Account]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Account'>SoftLayer_Notification_Occurrence_Account[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#impactedResources" name=impactedResources>impactedResources</a>
            </span>
            <div class='views-field-body'>A collection of resources impacted by this event. Each record will relate to some physical resource that the user has access to such as [[SoftLayer_Hardware]] or [[SoftLayer_Virtual_Guest]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Resource'>SoftLayer_Notification_Occurrence_Resource[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#impactedUsers" name=impactedUsers>impactedUsers</a>
            </span>
            <div class='views-field-body'>A collection of users impacted by this event. Each impacted user record relates directly to a [[SoftLayer_User_Customer]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Occurrence_User'>SoftLayer_Notification_Occurrence_User[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#lastUpdate" name=lastUpdate>lastUpdate</a>
            </span>
            <div class='views-field-body'>The last update for this event. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Update'>SoftLayer_Notification_Occurrence_Update </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notificationOccurrenceEventType" name=notificationOccurrenceEventType>notificationOccurrenceEventType</a>
            </span>
            <div class='views-field-body'>The type of event such as planned or unplanned maintenance. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event_Type'>SoftLayer_Notification_Occurrence_Event_Type </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#statusCode" name=statusCode>statusCode</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Status_Code'>SoftLayer_Notification_Occurrence_Status_Code </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#updates" name=updates>updates</a>
            </span>
            <div class='views-field-body'>All updates for this event. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Update'>SoftLayer_Notification_Occurrence_Update[] </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#attachmentCount" name=attachmentCount>attachmentCount</a>
            </span>
            <div class='views-field-body'>A count of a collection of attachments for this event which provide supplementary information to impacted users some examples are RFO (Reason For Outage) and root cause analysis documents. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#impactedAccountCount" name=impactedAccountCount>impactedAccountCount</a>
            </span>
            <div class='views-field-body'>A count of a collection of accounts impacted by this event. Each impacted account record relates directly to a [[SoftLayer_Account]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#impactedResourceCount" name=impactedResourceCount>impactedResourceCount</a>
            </span>
            <div class='views-field-body'>A count of a collection of resources impacted by this event. Each record will relate to some physical resource that the user has access to such as [[SoftLayer_Hardware]] or [[SoftLayer_Virtual_Guest]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#impactedUserCount" name=impactedUserCount>impactedUserCount</a>
            </span>
            <div class='views-field-body'>A count of a collection of users impacted by this event. Each impacted user record relates directly to a [[SoftLayer_User_Customer]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#updateCount" name=updateCount>updateCount</a>
            </span>
            <div class='views-field-body'>A count of all updates for this event. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>



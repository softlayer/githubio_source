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
[endDate]: #enddate
#### [endDate]
When this event will end.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique identifier for this event.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[lastImpactedUserCount]: #lastimpactedusercount
#### [lastImpactedUserCount]
Latest count of users impacted by this event.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
When this event was last updated.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[recoveryTime]: #recoverytime
#### [recoveryTime]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[startDate]: #startdate
#### [startDate]
When this event started.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[subject]: #subject
#### [subject]
Brief description of this event.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[summary]: #summary
#### [summary]
Details of this event.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[systemTicketId]: #systemticketid
#### [systemTicketId]
Unique identifier for the [SoftLayer_Ticket]({{<ref "reference/datatypes/SoftLayer_Ticket">}}) associated with this event.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[acknowledgedFlag]: #acknowledgedflag
#### [acknowledgedFlag]
Indicates whether or not this event has been acknowledged by the user.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[attachments]: #attachments
#### [attachments]
A collection of attachments for this event which provide supplementary information to impacted users some examples are RFO (Reason For Outage) and root cause analysis documents.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event_Attachment'>SoftLayer_Notification_Occurrence_Event_Attachment[] </a>**


</div>
<div class="prop-row">

-----
[firstUpdate]: #firstupdate
#### [firstUpdate]
The first update for this event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Update'>SoftLayer_Notification_Occurrence_Update </a>**


</div>
<div class="prop-row">

-----
[impactedAccounts]: #impactedaccounts
#### [impactedAccounts]
A collection of accounts impacted by this event. Each impacted account record relates directly to a [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Account'>SoftLayer_Notification_Occurrence_Account[] </a>**


</div>
<div class="prop-row">

-----
[impactedResources]: #impactedresources
#### [impactedResources]
A collection of resources impacted by this event. Each record will relate to some physical resource that the user has access to such as [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) or [SoftLayer_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Resource'>SoftLayer_Notification_Occurrence_Resource[] </a>**


</div>
<div class="prop-row">

-----
[impactedUsers]: #impactedusers
#### [impactedUsers]
A collection of users impacted by this event. Each impacted user record relates directly to a [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_User'>SoftLayer_Notification_Occurrence_User[] </a>**


</div>
<div class="prop-row">

-----
[lastUpdate]: #lastupdate
#### [lastUpdate]
The last update for this event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Update'>SoftLayer_Notification_Occurrence_Update </a>**


</div>
<div class="prop-row">

-----
[notificationOccurrenceEventType]: #notificationoccurrenceeventtype
#### [notificationOccurrenceEventType]
The type of event such as planned or unplanned maintenance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event_Type'>SoftLayer_Notification_Occurrence_Event_Type </a>**


</div>
<div class="prop-row">

-----
[statusCode]: #statuscode
#### [statusCode]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Status_Code'>SoftLayer_Notification_Occurrence_Status_Code </a>**


</div>
<div class="prop-row">

-----
[updates]: #updates
#### [updates]
All updates for this event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Update'>SoftLayer_Notification_Occurrence_Update[] </a>**


</div>

## Count
<div class="prop-row">

-----
[attachmentCount]: #attachmentcount
#### [attachmentCount]
A count of a collection of attachments for this event which provide supplementary information to impacted users some examples are RFO (Reason For Outage) and root cause analysis documents.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[impactedAccountCount]: #impactedaccountcount
#### [impactedAccountCount]
A count of a collection of accounts impacted by this event. Each impacted account record relates directly to a [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}).   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[impactedResourceCount]: #impactedresourcecount
#### [impactedResourceCount]
A count of a collection of resources impacted by this event. Each record will relate to some physical resource that the user has access to such as [SoftLayer_Hardware]({{<ref "reference/datatypes/SoftLayer_Hardware">}}) or [SoftLayer_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest">}}).   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[impactedUserCount]: #impactedusercount
#### [impactedUserCount]
A count of a collection of users impacted by this event. Each impacted user record relates directly to a [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}).   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[updateCount]: #updatecount
#### [updateCount]
A count of all updates for this event.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>



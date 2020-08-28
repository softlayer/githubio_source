---
title: "SoftLayer_Notification_User_Subscriber_Resource"
description: "Retrieve identifier cross-reference information.  SoftLayer_Notification_User_Subscriber_Resource provides the resource... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_User_Subscriber_Resource"
---

# SoftLayer_Notification_User_Subscriber_Resource
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber_Resource' >Datatype</a></li>
    </ul>
</div>

## Description 
Retrieve identifier cross-reference information.  SoftLayer_Notification_User_Subscriber_Resource provides the resource table id and subscriber id relation. The resource table id is the id of the service the subscriber receives alerts for.  This resource table id could be the unique identifier for a Storage Evault service or CDN service. 





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
[notificationUserSubscriberId]: #notificationusersubscriberid
#### [notificationUserSubscriberId]
Unique identifier of the subscriber that will receive the alerts for the resource subscribed to a notification.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
Unique identifier for a SoftLayer service that is subscribed to a notification.  Currently, the SoftLayer services that can be subscribed to notifications are: 

Storage EVault CDN 

  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[notificationUserSubscriber]: #notificationusersubscriber
#### [notificationUserSubscriber]
The Subscriber information tied to the resource service.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber </a>**


</div>

## Count
</div>



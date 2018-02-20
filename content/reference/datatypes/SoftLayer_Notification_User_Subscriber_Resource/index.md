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
Retrieve identifier cross-reference information.  SoftLayer_Notification_User_Subscriber_Resource provides the resource table id and subscriber id relation. The resource table id is the id of the service the subscriber receives alerts for.  This resource table id could be the unique identifier for a Storage Evault service, Global Load Balancer or CDN service. 
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
            <span class='views-field-title'><a href="#notificationUserSubscriberId" name=notificationUserSubscriberId>notificationUserSubscriberId</a></span>
            <div class='views-field-body'>Unique identifier of the subscriber that will receive the alerts for the resource subscribed to a notification.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resourceTableId" name=resourceTableId>resourceTableId</a></span>
            <div class='views-field-body'>Unique identifier for a SoftLayer service that is subscribed to a notification.  Currently, the SoftLayer services that can be subscribed to notifications are: 

Storage EVault CDN Global Load Balancer 

 </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notificationUserSubscriber" name=notificationUserSubscriber>notificationUserSubscriber</a></span>
            <div class='views-field-body'>The Subscriber information tied to the resource service. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber </a></p></div>
        </div>
            </div>
</div>



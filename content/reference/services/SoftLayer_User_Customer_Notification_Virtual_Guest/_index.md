---
title: "SoftLayer_User_Customer_Notification_Virtual_Guest"
description: "This service represents the link between a monitored guest instance, and a user account. 

When a monitoring service on... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
---
# SoftLayer_User_Customer_Notification_Virtual_Guest
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest' >Datatype</a></li>
    </ul>
</div>

## Description


This service represents the link between a monitored guest instance, and a user account. 

When a monitoring service on that guest instance fails and the monitor is set to "notify users," any users linked to that guest instance using this service will be notified of the failure. 



        
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

#### [createObject](/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/createObject)
Create a user virtual guest notification entry

</div>

<div class="method-row">

#### [createObjects](/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/createObjects)
Create multiple user Virtual Guest notification entries at once

</div>

<div class="method-row">

#### [deleteObjects](/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/deleteObjects)
Delete a group of SoftLayer_Customer_Notification_Virtual_Guest objects by passing in a collection of them

</div>

<div class="method-row">

#### [findByGuestId](/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/findByGuestId)
Return all CloudLayer computing instance notifications associated with the passed ID

</div>

<div class="method-row">

#### [getGuest](/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/getGuest)
Retrieve the virtual guest object that will be monitored.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/getObject)
Retrieve a SoftLayer_User_Customer_Notification_Virtual_Guest record.

</div>

<div class="method-row">

#### [getUser](/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/getUser)
Retrieve the user that will be notified when the associated virtual guest object fails a monitoring instance.

</div>
</div>

</div>


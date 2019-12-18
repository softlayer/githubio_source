---
title: "SoftLayer_User_Customer_Notification_Hardware"
description: "This service represents the link between a monitored hardware instance, and a user account. 

When a monitoring service... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Notification_Hardware"
---
# SoftLayer_User_Customer_Notification_Hardware
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_Notification_Hardware' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Hardware' >Datatype</a></li>
    </ul>
</div>

## Description
This service represents the link between a monitored hardware instance, and a user account. 

When a monitoring service on that hardware instance fails and the monitor is set to "notify users," any users linked to that hardware instance using this service will be notified of the failure. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [createObject](/reference/services/SoftLayer_User_Customer_Notification_Hardware/createObject)
Create a user hardware notification entry

#### [createObjects](/reference/services/SoftLayer_User_Customer_Notification_Hardware/createObjects)
Create multiple user hardware notification entries at once

#### [deleteObjects](/reference/services/SoftLayer_User_Customer_Notification_Hardware/deleteObjects)
Delete a group of Customer_Notification_Hardware objects by passing in a collection of them

#### [findByHardwareId](/reference/services/SoftLayer_User_Customer_Notification_Hardware/findByHardwareId)
Return all hardware notifications associated with the passed hardware ID

#### [getHardware](/reference/services/SoftLayer_User_Customer_Notification_Hardware/getHardware)
Retrieve the hardware object that will be monitored.

#### [getObject](/reference/services/SoftLayer_User_Customer_Notification_Hardware/getObject)
Retrieve a SoftLayer_User_Customer_Notification_Hardware record.

#### [getUser](/reference/services/SoftLayer_User_Customer_Notification_Hardware/getUser)
Retrieve the user that will be notified when the associated hardware object fails a monitoring instance.

</div>


---
title: "SoftLayer_User_Customer_Notification_Hardware"
description: "The Customer_Notification_Hardware object stores links between customers and the hardware devices they wish to monitor.... "
layout: "datatype"
tags:
    - "datatype"
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


The Customer_Notification_Hardware object stores links between customers and the hardware devices they wish to monitor.  This link is not enough, the user must be sure to also create SoftLayer_Network_Monitor_Version1_Query_Host instance with the response action set to "notify users" in order for the users linked to that hardware object to be notified on failure. 


### associatedMethods

*  [SoftLayer_User_Customer_Notification_Hardware::findByHardwareId](/reference/services/SoftLayer_User_Customer_Notification_Hardware/findByHardwareId )





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
[hardwareId]: #hardwareid
#### [hardwareId]
The ID of the Hardware object that is to be monitored.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique identifier for this object  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[userId]: #userid
#### [userId]
The ID of the SoftLayer_User_Customer object that represents the user to be notified on monitoring failure.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware object that will be monitored.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[user]: #user
#### [user]
The user that will be notified when the associated hardware object fails a monitoring instance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>

## Count
</div>



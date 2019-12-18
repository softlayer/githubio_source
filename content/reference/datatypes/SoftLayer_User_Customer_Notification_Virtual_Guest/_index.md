---
title: "SoftLayer_User_Customer_Notification_Virtual_Guest"
description: "The SoftLayer_User_Customer_Notification_Virtual_Guest object stores links between customers and the virtual guests they... "
layout: "datatype"
tags:
    - "datatype"
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
The SoftLayer_User_Customer_Notification_Virtual_Guest object stores links between customers and the virtual guests they wish to monitor.  This link is not enough, the user must be sure to also create SoftLayer_Network_Monitor_Version1_Query_Host instance with the response action set to "notify users" in order for the users linked to that hardware object to be notified on failure. 





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

## Local
-----
[guestId]: #guestid
#### [guestId]
The ID of the virtual guest object that is to be monitored.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
The unique identifier for this object  
<span class="type-label">Type: </span>**integer**

-----
[userId]: #userid
#### [userId]
The ID of the SoftLayer_User_Customer object that represents the user to be notified on monitoring failure.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[guest]: #guest
#### [guest]
The virtual guest object that will be monitored.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**

-----
[user]: #user
#### [user]
The user that will be notified when the associated virtual guest object fails a monitoring instance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


## Count
</div>



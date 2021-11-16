---
title: "SoftLayer_User_Customer_MobileDevice"
description: "This class represents a mobile device belonging to a user.  The device can be a phone, tablet, or possibly even some And... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_MobileDevice"
---

# SoftLayer_User_Customer_MobileDevice
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_MobileDevice' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_MobileDevice' >Datatype</a></li>
    </ul>
</div>

## Description 


This class represents a mobile device belonging to a user.  The device can be a phone, tablet, or possibly even some Android based net books.  The purpose is to tie just enough info with the device and the user to enable push notifications through non-softlayer entities (Google, Apple, RIM). 





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
[createDate]: #createdate
#### [createDate]
Created date for the record.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[displayResolutionXxY]: #displayresolutionxxy
#### [displayResolutionXxY]
The device resolution formatted width x height  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Record Identifier  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[mobileDeviceTypeId]: #mobiledevicetypeid
#### [mobileDeviceTypeId]
Device type identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[mobileOperatingSystemId]: #mobileoperatingsystemid
#### [mobileOperatingSystemId]
Mobile OS identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modelNumber]: #modelnumber
#### [modelNumber]
Device model number  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Last modify date for the record.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name of the device the user is using.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[phoneNumber]: #phonenumber
#### [phoneNumber]
Device phone number  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serialNumber]: #serialnumber
#### [serialNumber]
Device serial number  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[token]: #token
#### [token]
The token that is provided by the mobile device.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[userId]: #userid
#### [userId]
User Identifier  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[availablePushNotificationSubscriptions]: #availablepushnotificationsubscriptions
#### [availablePushNotificationSubscriptions]
Notification subscriptions available to a mobile device.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification'>SoftLayer_Notification[] </a>**  



</div>
<div class="prop-row">

-----
[customer]: #customer
#### [customer]
The user this mobile device belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>
<div class="prop-row">

-----
[operatingSystem]: #operatingsystem
#### [operatingSystem]
The operating system this device is using  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_MobileDevice_OperatingSystem'>SoftLayer_User_Customer_MobileDevice_OperatingSystem </a>**  



</div>
<div class="prop-row">

-----
[pushNotificationSubscriptions]: #pushnotificationsubscriptions
#### [pushNotificationSubscriptions]
Notification subscriptions attached to a mobile device.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber[] </a>**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of device this user is using  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_MobileDevice_Type'>SoftLayer_User_Customer_MobileDevice_Type </a>**  



</div>

## Count
<div class="prop-row">

-----
[availablePushNotificationSubscriptionCount]: #availablepushnotificationsubscriptioncount
#### [availablePushNotificationSubscriptionCount]
A count of notification subscriptions available to a mobile device.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[pushNotificationSubscriptionCount]: #pushnotificationsubscriptioncount
#### [pushNotificationSubscriptionCount]
A count of notification subscriptions attached to a mobile device.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>



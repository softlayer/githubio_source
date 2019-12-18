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
[createDate]: #createdate
#### [createDate]
Created date for the record.  
<span class="type-label">Type: </span>**dateTime**

-----
[displayResolutionXxY]: #displayresolutionxxy
#### [displayResolutionXxY]
The device resolution formatted width x height  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
Record Identifier  
<span class="type-label">Type: </span>**integer**

-----
[mobileDeviceTypeId]: #mobiledevicetypeid
#### [mobileDeviceTypeId]
Device type identifier.  
<span class="type-label">Type: </span>**integer**

-----
[mobileOperatingSystemId]: #mobileoperatingsystemid
#### [mobileOperatingSystemId]
Mobile OS identifier.  
<span class="type-label">Type: </span>**integer**

-----
[modelNumber]: #modelnumber
#### [modelNumber]
Device model number  
<span class="type-label">Type: </span>**string**

-----
[modifyDate]: #modifydate
#### [modifyDate]
Last modify date for the record.  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
The name of the device the user is using.  
<span class="type-label">Type: </span>**string**

-----
[phoneNumber]: #phonenumber
#### [phoneNumber]
Device phone number  
<span class="type-label">Type: </span>**string**

-----
[serialNumber]: #serialnumber
#### [serialNumber]
Device serial number  
<span class="type-label">Type: </span>**string**

-----
[token]: #token
#### [token]
The token that is provided by the mobile device.  
<span class="type-label">Type: </span>**string**

-----
[userId]: #userid
#### [userId]
User Identifier  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[availablePushNotificationSubscriptions]: #availablepushnotificationsubscriptions
#### [availablePushNotificationSubscriptions]
Notification subscriptions available to a mobile device.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification'>SoftLayer_Notification[] </a>**

-----
[customer]: #customer
#### [customer]
The user this mobile device belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[operatingSystem]: #operatingsystem
#### [operatingSystem]
The operating system this device is using  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_MobileDevice_OperatingSystem'>SoftLayer_User_Customer_MobileDevice_OperatingSystem </a>**

-----
[pushNotificationSubscriptions]: #pushnotificationsubscriptions
#### [pushNotificationSubscriptions]
Notification subscriptions attached to a mobile device.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber[] </a>**

-----
[type]: #type
#### [type]
The type of device this user is using  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_MobileDevice_Type'>SoftLayer_User_Customer_MobileDevice_Type </a>**


## Count

-----
[availablePushNotificationSubscriptionCount]: #availablepushnotificationsubscriptioncount
#### [availablePushNotificationSubscriptionCount]
A count of notification subscriptions available to a mobile device.   
<span class="type-label">Type: </span>**unsigned long**


-----
[pushNotificationSubscriptionCount]: #pushnotificationsubscriptioncount
#### [pushNotificationSubscriptionCount]
A count of notification subscriptions attached to a mobile device.   
<span class="type-label">Type: </span>**unsigned long**

</div>



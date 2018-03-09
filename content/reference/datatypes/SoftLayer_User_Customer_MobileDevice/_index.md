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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>Created date for the record. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#displayResolutionXxY" name=displayResolutionXxY>displayResolutionXxY</a>
            </span>
            <div class='views-field-body'>The device resolution formatted width x height </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>Record Identifier </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#mobileDeviceTypeId" name=mobileDeviceTypeId>mobileDeviceTypeId</a>
            </span>
            <div class='views-field-body'>Device type identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#mobileOperatingSystemId" name=mobileOperatingSystemId>mobileOperatingSystemId</a>
            </span>
            <div class='views-field-body'>Mobile OS identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modelNumber" name=modelNumber>modelNumber</a>
            </span>
            <div class='views-field-body'>Device model number </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>Last modify date for the record. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>The name of the device the user is using. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#phoneNumber" name=phoneNumber>phoneNumber</a>
            </span>
            <div class='views-field-body'>Device phone number </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#serialNumber" name=serialNumber>serialNumber</a>
            </span>
            <div class='views-field-body'>Device serial number </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#token" name=token>token</a>
            </span>
            <div class='views-field-body'>The token that is provided by the mobile device. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userId" name=userId>userId</a>
            </span>
            <div class='views-field-body'>User Identifier </div>
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
                <a href="#availablePushNotificationSubscriptions" name=availablePushNotificationSubscriptions>availablePushNotificationSubscriptions</a>
            </span>
            <div class='views-field-body'>Notification subscriptions available to a mobile device. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification'>SoftLayer_Notification[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#customer" name=customer>customer</a>
            </span>
            <div class='views-field-body'>The user this mobile device belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#operatingSystem" name=operatingSystem>operatingSystem</a>
            </span>
            <div class='views-field-body'>The operating system this device is using </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_MobileDevice_OperatingSystem'>SoftLayer_User_Customer_MobileDevice_OperatingSystem </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#pushNotificationSubscriptions" name=pushNotificationSubscriptions>pushNotificationSubscriptions</a>
            </span>
            <div class='views-field-body'>Notification subscriptions attached to a mobile device. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#type" name=type>type</a>
            </span>
            <div class='views-field-body'>The type of device this user is using </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_MobileDevice_Type'>SoftLayer_User_Customer_MobileDevice_Type </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#availablePushNotificationSubscriptionCount" name=availablePushNotificationSubscriptionCount>availablePushNotificationSubscriptionCount</a>
            </span>
            <div class='views-field-body'>A count of notification subscriptions available to a mobile device. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#pushNotificationSubscriptionCount" name=pushNotificationSubscriptionCount>pushNotificationSubscriptionCount</a>
            </span>
            <div class='views-field-body'>A count of notification subscriptions attached to a mobile device. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>



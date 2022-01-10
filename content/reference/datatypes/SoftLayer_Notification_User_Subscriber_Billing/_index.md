---
title: "SoftLayer_Notification_User_Subscriber_Billing"
description: "A notification subscriber will have details pertaining to the subscriber's notification subscription.  You can receive d... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_User_Subscriber_Billing"
---

# SoftLayer_Notification_User_Subscriber_Billing
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Notification_User_Subscriber_Billing' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber_Billing' >Datatype</a></li>
    </ul>
</div>

## Description 


A notification subscriber will have details pertaining to the subscriber's notification subscription.  You can receive details such as preferences, details of the preferences, delivery methods and the delivery methods for the subscriber. 

NOTE: There are preferences and delivery methods that cannot be modified.  Also, there are some subscriptions that are required. 


### associatedMethods

*  [SoftLayer_Notification::getObject](/reference/services/SoftLayer_Notification/getObject )





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
[active]: #active
#### [active]
The current status of the subscription.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique identifier of the subscriber that will receive the alerts.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[notificationId]: #notificationid
#### [notificationId]
Unique identifier of the notification subscribed to.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[userRecordId]: #userrecordid
#### [userRecordId]
Unique identifier of the user the subscription is for.   
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[deliveryMethods]: #deliverymethods
#### [deliveryMethods]
The delivery methods used to send the subscribed notification.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Delivery_Method'>SoftLayer_Notification_Delivery_Method[] </a>**  



</div>
<div class="prop-row">

-----
[notification]: #notification
#### [notification]
Notification subscribed to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification'>SoftLayer_Notification </a>**  



</div>
<div class="prop-row">

-----
[preferences]: #preferences
#### [preferences]
Associated subscriber preferences used for the notification subscription. For example, preferences include number of deliveries (limit) and threshold.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber_Preference'>SoftLayer_Notification_User_Subscriber_Preference[] </a>**  



</div>
<div class="prop-row">

-----
[preferencesDetails]: #preferencesdetails
#### [preferencesDetails]
Preference details such as description, minimum and maximum limits, default value and unit of measure.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Preference'>SoftLayer_Notification_Preference[] </a>**  



</div>
<div class="prop-row">

-----
[resourceRecord]: #resourcerecord
#### [resourceRecord]
The subscriber id to resource id mapping.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber_Resource'>SoftLayer_Notification_User_Subscriber_Resource </a>**  



</div>
<div class="prop-row">

-----
[userRecord]: #userrecord
#### [userRecord]
User record for the subscription.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>

## Count
<div class="prop-row">

-----
[deliveryMethodCount]: #deliverymethodcount
#### [deliveryMethodCount]
A count of the delivery methods used to send the subscribed notification.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[preferenceCount]: #preferencecount
#### [preferenceCount]
A count of associated subscriber preferences used for the notification subscription. For example, preferences include number of deliveries (limit) and threshold.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[preferencesDetailCount]: #preferencesdetailcount
#### [preferencesDetailCount]
A count of preference details such as description, minimum and maximum limits, default value and unit of measure.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>



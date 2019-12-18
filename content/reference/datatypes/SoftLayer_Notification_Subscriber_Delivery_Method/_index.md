---
title: "SoftLayer_Notification_Subscriber_Delivery_Method"
description: "Provides details for the subscriber's delivery methods."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Subscriber_Delivery_Method"
---

# SoftLayer_Notification_Subscriber_Delivery_Method
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_Subscriber_Delivery_Method' >Datatype</a></li>
    </ul>
</div>

## Description 
Provides details for the subscriber's delivery methods. 





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
[active]: #active
#### [active]
Indicates the subscriber's delivery method availability for notifications.   
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
Date the subscriber's delivery method was created.   
<span class="type-label">Type: </span>**dateTime**

-----
[modifyDate]: #modifydate
#### [modifyDate]
Date the subscriber's delivery method was last modified.   
<span class="type-label">Type: </span>**dateTime**

-----
[notificationDeliveryMethodId]: #notificationdeliverymethodid
#### [notificationDeliveryMethodId]
Identifier for the notification delivery method.   
<span class="type-label">Type: </span>**integer**

-----
[notificationSubscriberId]: #notificationsubscriberid
#### [notificationSubscriberId]
Identifier for the subscriber.   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[notificationDeliveryMethod]: #notificationdeliverymethod
#### [notificationDeliveryMethod]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Delivery_Method'>SoftLayer_Notification_Delivery_Method </a>**

-----
[notificationSubscriber]: #notificationsubscriber
#### [notificationSubscriber]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Subscriber'>SoftLayer_Notification_Subscriber </a>**


## Count
</div>



---
title: "SoftLayer_Notification_User_Subscriber_Delivery_Method"
description: "Provides mapping details of how the subscriber's notification will be delivered.  This maps the subscriber's id with all... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_User_Subscriber_Delivery_Method"
---

# SoftLayer_Notification_User_Subscriber_Delivery_Method
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber_Delivery_Method' >Datatype</a></li>
    </ul>
</div>

## Description 
Provides mapping details of how the subscriber's notification will be delivered.  This maps the subscriber's id with all the delivery method ids used to delivery the notification. 





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
Determines if the delivery method is active for the user.   
<span class="type-label">Type: </span>**integer**

-----
[notificationMethodId]: #notificationmethodid
#### [notificationMethodId]
Unique identifier of the method used to deliver notification.   
<span class="type-label">Type: </span>**integer**

-----
[notificationUserSubscriberId]: #notificationusersubscriberid
#### [notificationUserSubscriberId]
Unique identifier of the subscriber tied to the delivery method.   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[deliveryMethod]: #deliverymethod
#### [deliveryMethod]
Provides details for the method used to deliver the notification (email, sms, ticket).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Delivery_Method'>SoftLayer_Notification_Delivery_Method </a>**

-----
[notificationUserSubscriber]: #notificationusersubscriber
#### [notificationUserSubscriber]
The Subscriber information tied to the delivery method.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber </a>**


## Count
</div>



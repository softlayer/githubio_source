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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#active" name=active>active</a></span>
            <div class='views-field-body'>Determines if the delivery method is active for the user.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notificationMethodId" name=notificationMethodId>notificationMethodId</a></span>
            <div class='views-field-body'>Unique identifier of the method used to deliver notification.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notificationUserSubscriberId" name=notificationUserSubscriberId>notificationUserSubscriberId</a></span>
            <div class='views-field-body'>Unique identifier of the subscriber tied to the delivery method.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deliveryMethod" name=deliveryMethod>deliveryMethod</a></span>
            <div class='views-field-body'>Provides details for the method used to deliver the notification (email, sms, ticket). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Notification_Delivery_Method'>SoftLayer_Notification_Delivery_Method </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notificationUserSubscriber" name=notificationUserSubscriber>notificationUserSubscriber</a></span>
            <div class='views-field-body'>The Subscriber information tied to the delivery method. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>



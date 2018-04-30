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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#active" name=active>active</a>
            </span>
            <div class='views-field-body'>Indicates the subscriber's delivery method availability for notifications.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>Date the subscriber's delivery method was created.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>Date the subscriber's delivery method was last modified.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notificationDeliveryMethodId" name=notificationDeliveryMethodId>notificationDeliveryMethodId</a>
            </span>
            <div class='views-field-body'>Identifier for the notification delivery method.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notificationSubscriberId" name=notificationSubscriberId>notificationSubscriberId</a>
            </span>
            <div class='views-field-body'>Identifier for the subscriber.  </div>
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
                <a href="#notificationDeliveryMethod" name=notificationDeliveryMethod>notificationDeliveryMethod</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Delivery_Method'>SoftLayer_Notification_Delivery_Method </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notificationSubscriber" name=notificationSubscriber>notificationSubscriber</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Subscriber'>SoftLayer_Notification_Subscriber </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>



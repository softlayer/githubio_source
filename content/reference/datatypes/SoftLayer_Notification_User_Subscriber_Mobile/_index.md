---
title: "SoftLayer_Notification_User_Subscriber_Mobile"
description: "A notification subscriber will have details pertaining to the subscriber's notification subscription.  You can receive d... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_User_Subscriber_Mobile"
---

# SoftLayer_Notification_User_Subscriber_Mobile
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Notification_User_Subscriber_Mobile' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber_Mobile' >Datatype</a></li>
    </ul>
</div>

## Description 
A notification subscriber will have details pertaining to the subscriber's notification subscription.  You can receive details such as preferences, details of the preferences, delivery methods and the delivery methods for the subscriber. 

NOTE: There are preferences and delivery methods that cannot be modified.  Also, there are some subscriptions that are required. 


### associatedMethods

*  [SoftLayer_Notification::getObject](/reference/services/SoftLayer_Notification/getObject )





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
            <div class='views-field-body'>The current status of the subscription.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>Unique identifier of the subscriber that will receive the alerts.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notificationId" name=notificationId>notificationId</a>
            </span>
            <div class='views-field-body'>Unique identifier of the notification subscribed to.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userRecordId" name=userRecordId>userRecordId</a>
            </span>
            <div class='views-field-body'>Unique identifier of the user the subscription is for.  </div>
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
                <a href="#deliveryMethods" name=deliveryMethods>deliveryMethods</a>
            </span>
            <div class='views-field-body'>The delivery methods used to send the subscribed notification. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Delivery_Method'>SoftLayer_Notification_Delivery_Method[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notification" name=notification>notification</a>
            </span>
            <div class='views-field-body'>Notification subscribed to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification'>SoftLayer_Notification </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#preferences" name=preferences>preferences</a>
            </span>
            <div class='views-field-body'>Associated subscriber preferences used for the notification subscription. For example, preferences include number of deliveries (limit) and threshold. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber_Preference'>SoftLayer_Notification_User_Subscriber_Preference[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#preferencesDetails" name=preferencesDetails>preferencesDetails</a>
            </span>
            <div class='views-field-body'>Preference details such as description, minimum and maximum limits, default value and unit of measure. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Preference'>SoftLayer_Notification_Preference[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resourceRecord" name=resourceRecord>resourceRecord</a>
            </span>
            <div class='views-field-body'>The subscriber id to resource id mapping. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber_Resource'>SoftLayer_Notification_User_Subscriber_Resource </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userRecord" name=userRecord>userRecord</a>
            </span>
            <div class='views-field-body'>User record for the subscription. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#deliveryMethodCount" name=deliveryMethodCount>deliveryMethodCount</a>
            </span>
            <div class='views-field-body'>A count of the delivery methods used to send the subscribed notification. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#preferenceCount" name=preferenceCount>preferenceCount</a>
            </span>
            <div class='views-field-body'>A count of associated subscriber preferences used for the notification subscription. For example, preferences include number of deliveries (limit) and threshold. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#preferencesDetailCount" name=preferencesDetailCount>preferencesDetailCount</a>
            </span>
            <div class='views-field-body'>A count of preference details such as description, minimum and maximum limits, default value and unit of measure. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>



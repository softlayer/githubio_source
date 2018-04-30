---
title: "SoftLayer_Notification_User_Subscriber_Preference"
description: "Preferences are settings that can be modified to change the behavior of the subscription.  For example, modify the limit... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_User_Subscriber_Preference"
---

# SoftLayer_Notification_User_Subscriber_Preference
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Notification_User_Subscriber_Preference' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber_Preference' >Datatype</a></li>
    </ul>
</div>

## Description 
Preferences are settings that can be modified to change the behavior of the subscription.  For example, modify the limit preference to only receive notifications 10 times instead of 1 during a billing cycle. 

NOTE: Some preferences have certain restrictions on values that can be set. 


### associatedMethods

*  [SoftLayer_Notification_User_Subscriber::editObject](/reference/services/SoftLayer_Notification_User_Subscriber/editObject )





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
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>Unique identifier for the subscriber's preferences.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notificationPreferenceId" name=notificationPreferenceId>notificationPreferenceId</a>
            </span>
            <div class='views-field-body'>Unique identifier of the default preference for which the subscriber preference is based on.  For example, if no preferences are supplied during the creation of a subscriber.  The default values are pulled using this property.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notificationUserSubscriberId" name=notificationUserSubscriberId>notificationUserSubscriberId</a>
            </span>
            <div class='views-field-body'>Unique identifier of the subscriber tied to the subscriber preference.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#value" name=value>value</a>
            </span>
            <div class='views-field-body'>The user supplied value to "override" the "default" preference's value.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#defaultPreference" name=defaultPreference>defaultPreference</a>
            </span>
            <div class='views-field-body'>Details such name, keyname, minimum and maximum values for the preference. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Preference'>SoftLayer_Notification_Preference </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notificationUserSubscriber" name=notificationUserSubscriber>notificationUserSubscriber</a>
            </span>
            <div class='views-field-body'>Details of the subscriber tied to the preference. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>



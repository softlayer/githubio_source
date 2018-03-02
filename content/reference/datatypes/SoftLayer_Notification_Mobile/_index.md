---
title: "SoftLayer_Notification_Mobile"
description: "This is an extension of the SoftLayer_Notification class.  These are implementation details specific to those notificati... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Mobile"
---

# SoftLayer_Notification_Mobile
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_Mobile' >Datatype</a></li>
    </ul>
</div>

## Description 
This is an extension of the SoftLayer_Notification class.  These are implementation details specific to those notifications which can be subscribed to and received on a mobile device. 





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
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>Unique identifier for the notification.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keyName" name=keyName>keyName</a></span>
            <div class='views-field-body'>Name that can be used by external systems to refer to a notification.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>Friendly name for the notification.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#preferences" name=preferences>preferences</a></span>
            <div class='views-field-body'>The preferences related to the notification. These are preferences are configurable and optional for subscribers to use. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Notification_Preference'>SoftLayer_Notification_Preference[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#requiredPreferences" name=requiredPreferences>requiredPreferences</a></span>
            <div class='views-field-body'>The required preferences related to the notification. While configurable, the subscriber does not have the option whether to use the preference. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Notification_Preference'>SoftLayer_Notification_Preference[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#preferenceCount" name=preferenceCount>preferenceCount</a></span>
            <div class='views-field-body'>A count of the preferences related to the notification. These are preferences are configurable and optional for subscribers to use. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#requiredPreferenceCount" name=requiredPreferenceCount>requiredPreferenceCount</a></span>
            <div class='views-field-body'>A count of the required preferences related to the notification. While configurable, the subscriber does not have the option whether to use the preference. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>



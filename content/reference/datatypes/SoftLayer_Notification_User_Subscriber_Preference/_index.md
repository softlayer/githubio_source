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
[id]: #id
#### [id]
Unique identifier for the subscriber's preferences.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[notificationPreferenceId]: #notificationpreferenceid
#### [notificationPreferenceId]
Unique identifier of the default preference for which the subscriber preference is based on.  For example, if no preferences are supplied during the creation of a subscriber.  The default values are pulled using this property.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[notificationUserSubscriberId]: #notificationusersubscriberid
#### [notificationUserSubscriberId]
Unique identifier of the subscriber tied to the subscriber preference.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[value]: #value
#### [value]
The user supplied value to "override" the "default" preference's value.   
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[defaultPreference]: #defaultpreference
#### [defaultPreference]
Details such name, keyname, minimum and maximum values for the preference.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Preference'>SoftLayer_Notification_Preference </a>**  



</div>
<div class="prop-row">

-----
[notificationUserSubscriber]: #notificationusersubscriber
#### [notificationUserSubscriber]
Details of the subscriber tied to the preference.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber </a>**  



</div>

## Count
</div>



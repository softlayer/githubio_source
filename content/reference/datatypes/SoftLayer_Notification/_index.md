---
title: "SoftLayer_Notification"
description: "Details provided for the notification are basic.  Details such as the related preferences, name and keyname for the noti... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification"
---

# SoftLayer_Notification
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Notification' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification' >Datatype</a></li>
    </ul>
</div>

## Description 


Details provided for the notification are basic.  Details such as the related preferences, name and keyname for the notification can be retrieved.  The keyname property for the notification can be used to refer to a notification when integrating into the SoftLayer Notification system.  The name property can used more for display purposes. 





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
Unique identifier for the notification.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
Name that can be used by external systems to refer to a notification.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Friendly name for the notification.   
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[preferences]: #preferences
#### [preferences]
The preferences related to the notification. These are preferences are configurable and optional for subscribers to use.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Preference'>SoftLayer_Notification_Preference[] </a>**  



</div>
<div class="prop-row">

-----
[requiredPreferences]: #requiredpreferences
#### [requiredPreferences]
The required preferences related to the notification. While configurable, the subscriber does not have the option whether to use the preference.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Preference'>SoftLayer_Notification_Preference[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[preferenceCount]: #preferencecount
#### [preferenceCount]
A count of the preferences related to the notification. These are preferences are configurable and optional for subscribers to use.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[requiredPreferenceCount]: #requiredpreferencecount
#### [requiredPreferenceCount]
A count of the required preferences related to the notification. While configurable, the subscriber does not have the option whether to use the preference.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>



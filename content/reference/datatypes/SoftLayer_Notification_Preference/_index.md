---
title: "SoftLayer_Notification_Preference"
description: "Retrieve details for preferences.  Preferences are used to allow the subscriber to modify their subscription in various... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Preference"
---

# SoftLayer_Notification_Preference
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_Preference' >Datatype</a></li>
    </ul>
</div>

## Description 
Retrieve details for preferences.  Preferences are used to allow the subscriber to modify their subscription in various ways.  Details such as friendly name, keyname maximum and minimum values can be retrieved.  These provide details to help configure subscriber preferences correctly. 





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
[description]: #description
#### [description]
A description of what the preference is used for.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique identifier for the notification preference.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
Name that can be used by external systems to refer to preference.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[maximumValue]: #maximumvalue
#### [maximumValue]
Largest value allowed for the preference.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[minimumValue]: #minimumvalue
#### [minimumValue]
Smallest value allowed for the preference.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Friendly name for the notification.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[units]: #units
#### [units]
The unit of measure used for the preference's value, minimum and maximum as well.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[value]: #value
#### [value]
Default value used when setting up preferences for a new subscriber.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>



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
[description]: #description
#### [description]
A description of what the preference is used for.   
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
Unique identifier for the notification preference.   
<span class="type-label">Type: </span>**integer**

-----
[keyName]: #keyname
#### [keyName]
Name that can be used by external systems to refer to preference.   
<span class="type-label">Type: </span>**string**

-----
[maximumValue]: #maximumvalue
#### [maximumValue]
Largest value allowed for the preference.   
<span class="type-label">Type: </span>**string**

-----
[minimumValue]: #minimumvalue
#### [minimumValue]
Smallest value allowed for the preference.   
<span class="type-label">Type: </span>**string**

-----
[name]: #name
#### [name]
Friendly name for the notification.   
<span class="type-label">Type: </span>**string**

-----
[units]: #units
#### [units]
The unit of measure used for the preference's value, minimum and maximum as well.   
<span class="type-label">Type: </span>**string**

-----
[value]: #value
#### [value]
Default value used when setting up preferences for a new subscriber.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>



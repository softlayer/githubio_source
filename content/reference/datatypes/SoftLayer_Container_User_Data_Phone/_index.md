---
title: "SoftLayer_Container_User_Data_Phone"
description: "This container holds user's phone information."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_User_Data_Phone"
---

# SoftLayer_Container_User_Data_Phone
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_User_Data_Phone' >Datatype</a></li>
    </ul>
</div>

## Description 
This container holds user's phone information. 





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
[countryCode]: #countrycode
#### [countryCode]
Country code number for the phone number Default: 1 (United States & Canada +1)   
<span class="type-label">Type: </span>**integer**

-----
[extension]: #extension
#### [extension]
Phone extension code. It can be digits, commas, *, and # are allowed.   
<span class="type-label">Type: </span>**string**

-----
[phone]: #phone
#### [phone]
Phone number can be a mobile phone number, desk phone number, or some other option. The phone number format must match the format selected in the country code.   
<span class="type-label">Type: </span>**string**

-----
[phoneType]: #phonetype
#### [phoneType]
Type of phone number such as "primary", "office" or "home"   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>



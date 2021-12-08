---
title: "SoftLayer_Locale_Timezone"
description: "Each User is assigned a timezone allowing for a precise local timestamp."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Locale"
classes:
    - "SoftLayer_Locale_Timezone"
---

# SoftLayer_Locale_Timezone
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Locale_Timezone' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Locale_Timezone' >Datatype</a></li>
    </ul>
</div>

## Description 


Each User is assigned a timezone allowing for a precise local timestamp.


### associatedMethods

*  [SoftLayer_User_Customer::getTimezone](/reference/services/SoftLayer_User_Customer/getTimezone )



### seeAlso

* [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer )




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
A timezone's identifying number.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[longName]: #longname
#### [longName]
A timezone's long name. For example, "(GMT-06:00) America/Dallas - CST".  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A timezone's name. For example, "America/Dallas".  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[offset]: #offset
#### [offset]
A timezone's offset based on the GMT standard. For example, Central Standard Time's offset is "-0600" from GMT=0000.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[shortName]: #shortname
#### [shortName]
A timezone's common abbreviation. For example, Central Standard Time's abbreviation is "CST".  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>



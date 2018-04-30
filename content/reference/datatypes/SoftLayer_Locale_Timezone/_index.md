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
            <div class='views-field-body'>A timezone's identifying number. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#longName" name=longName>longName</a>
            </span>
            <div class='views-field-body'>A timezone's long name. For example, "(GMT-06:00) America/Dallas - CST". </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>A timezone's name. For example, "America/Dallas". </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#offset" name=offset>offset</a>
            </span>
            <div class='views-field-body'>A timezone's offset based on the GMT standard. For example, Central Standard Time's offset is "-0600" from GMT=0000. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#shortName" name=shortName>shortName</a>
            </span>
            <div class='views-field-body'>A timezone's common abbreviation. For example, Central Standard Time's abbreviation is "CST". </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>



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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#countryCode" name=countryCode>countryCode</a></span>
            <div class='views-field-body'>Country code number for the phone number Default: 1 (United States & Canada +1)  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#extension" name=extension>extension</a></span>
            <div class='views-field-body'>Phone extension code. It can be digits, commas, *, and # are allowed.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#phone" name=phone>phone</a></span>
            <div class='views-field-body'>Phone number can be a mobile phone number, desk phone number, or some other option. The phone number format must match the format selected in the country code.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#phoneType" name=phoneType>phoneType</a></span>
            <div class='views-field-body'>Type of phone number such as "primary", "office" or "home"  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>



---
title: "SoftLayer_Layout_Preference"
description: "The SoftLayer_Layout_Preference contains definitions for default layout item preferences"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Preference"
---

# SoftLayer_Layout_Preference
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Preference' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Layout_Preference contains definitions for default layout item preferences 





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
            <div class='views-field-body'>The internal identifier of a layout preference </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutPreferenceTypeId" name=layoutPreferenceTypeId>layoutPreferenceTypeId</a></span>
            <div class='views-field-body'>The internal identifier of the related [[SoftLayer_Layout_Preference_Type]] </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#value" name=value>value</a></span>
            <div class='views-field-body'>The default value of the preference </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutPreferenceType" name=layoutPreferenceType>layoutPreferenceType</a></span>
            <div class='views-field-body'>The type of the preference object </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Layout_Preference_Type'>SoftLayer_Layout_Preference_Type </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>



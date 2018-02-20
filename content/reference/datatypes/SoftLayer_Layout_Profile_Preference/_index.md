---
title: "SoftLayer_Layout_Profile_Preference"
description: "The SoftLayer_Layout_Profile_Preference contains definitions for layout preferences"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile_Preference"
---

# SoftLayer_Layout_Profile_Preference
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Layout_Profile_Preference' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Profile_Preference' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Layout_Profile_Preference contains definitions for layout preferences 
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
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>Timestamp of when the preference was created </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#defaultValueFlag" name=defaultValueFlag>defaultValueFlag</a></span>
            <div class='views-field-body'>Indicates whether this is a default value or not </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutContainerId" name=layoutContainerId>layoutContainerId</a></span>
            <div class='views-field-body'>The id of the related [[SoftLayer_Layout_Container]] </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutItemId" name=layoutItemId>layoutItemId</a></span>
            <div class='views-field-body'>The id of the related [[SoftLayer_Layout_Item]] </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutPreferenceId" name=layoutPreferenceId>layoutPreferenceId</a></span>
            <div class='views-field-body'>The internal identifier of the overridden [[SoftLayer_Layout_Preference]] </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutProfileId" name=layoutProfileId>layoutProfileId</a></span>
            <div class='views-field-body'>The internal identifier of the related [[SoftLayer_Layout_Profile]] </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>Timestamp of when the preference was last updated </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#value" name=value>value</a></span>
            <div class='views-field-body'>The value overriding the default value </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutContainer" name=layoutContainer>layoutContainer</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Layout_Container'>SoftLayer_Layout_Container </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutItem" name=layoutItem>layoutItem</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Layout_Item'>SoftLayer_Layout_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutPreference" name=layoutPreference>layoutPreference</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Layout_Preference'>SoftLayer_Layout_Preference </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutProfile" name=layoutProfile>layoutProfile</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Layout_Profile'>SoftLayer_Layout_Profile </a></p></div>
        </div>
            </div>
</div>



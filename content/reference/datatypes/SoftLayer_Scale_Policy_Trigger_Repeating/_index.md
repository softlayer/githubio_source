---
title: "SoftLayer_Scale_Policy_Trigger_Repeating"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Policy_Trigger_Repeating"
---

# SoftLayer_Scale_Policy_Trigger_Repeating
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger_Repeating' >Datatype</a></li>
    </ul>
</div>

## Description 






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
            <div class='views-field-body'>When this trigger was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deleteFlag" name=deleteFlag>deleteFlag</a></span>
            <div class='views-field-body'>When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A trigger's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>When this trigger was last modified. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#scalePolicyId" name=scalePolicyId>scalePolicyId</a></span>
            <div class='views-field-body'>The policy this trigger is on. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#schedule" name=schedule>schedule</a></span>
            <div class='views-field-body'>The cron-formatted schedule. This is run in the UTC timezone. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#typeId" name=typeId>typeId</a></span>
            <div class='views-field-body'>The type of trigger this is. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#scalePolicy" name=scalePolicy>scalePolicy</a></span>
            <div class='views-field-body'>The policy this trigger is on. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Policy'>SoftLayer_Scale_Policy </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>The type of trigger. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger_Type'>SoftLayer_Scale_Policy_Trigger_Type </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>



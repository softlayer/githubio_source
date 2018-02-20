---
title: "SoftLayer_Layout_Item"
description: "The SoftLayer_Layout_Item contains definitions for default layout items"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Item"
---

# SoftLayer_Layout_Item
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Layout_Item' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Item' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Layout_Item contains definitions for default layout items 
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
            <div class='views-field-body'>The internal identifier of a layout item </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keyname" name=keyname>keyname</a></span>
            <div class='views-field-body'>The unique key name of the layout item, used primarily for programmatic purposes </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutItemTypeId" name=layoutItemTypeId>layoutItemTypeId</a></span>
            <div class='views-field-body'>The internal identifier of the related [[SoftLayer_Layout_Item_Type]] </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The friendly name of the layout item </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutItemPreferences" name=layoutItemPreferences>layoutItemPreferences</a></span>
            <div class='views-field-body'>The layout preferences assigned to this layout item </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Layout_Preference'>SoftLayer_Layout_Preference[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutItemType" name=layoutItemType>layoutItemType</a></span>
            <div class='views-field-body'>The type of the layout item object </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Layout_Item_Type'>SoftLayer_Layout_Item_Type </a></p></div>
        </div>
            </div>
</div>



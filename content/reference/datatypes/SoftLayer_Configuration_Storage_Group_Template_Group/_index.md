---
title: "SoftLayer_Configuration_Storage_Group_Template_Group"
description: "Single storage group(array) used in a storage group template. 

If a server configuration requires a raid configuration... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Configuration"
classes:
    - "SoftLayer_Configuration_Storage_Group_Template_Group"
---

# SoftLayer_Configuration_Storage_Group_Template_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Template_Group' >Datatype</a></li>
    </ul>
</div>

## Description 
Single storage group(array) used in a storage group template. 

If a server configuration requires a raid configuration this object will describe a single array to be configured. 





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
            <span class='views-field-title'><a href="#diskControllerIndex" name=diskControllerIndex>diskControllerIndex</a></span>
            <div class='views-field-body'>The disk controller for the array. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#grow" name=grow>grow</a></span>
            <div class='views-field-body'>Flag to use all available space. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardDrivesString" name=hardDrivesString>hardDrivesString</a></span>
            <div class='views-field-body'>Comma delimited integers of drive indexes for the array. This can also be the string 'all' to specify all drives in the server  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hotSpareDrivesString" name=hotSpareDrivesString>hotSpareDrivesString</a></span>
            <div class='views-field-body'>Comma delimited integers of drive indexes for hot spares on the array.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderIndex" name=orderIndex>orderIndex</a></span>
            <div class='views-field-body'>The order of the arrays in the template. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#size" name=size>size</a></span>
            <div class='views-field-body'>Size of array. Must be within limitations of the smallest drive and raid mode </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Array_Type'>SoftLayer_Configuration_Storage_Group_Array_Type </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>



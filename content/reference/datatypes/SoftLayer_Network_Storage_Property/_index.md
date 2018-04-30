---
title: "SoftLayer_Network_Storage_Property"
description: "A property provides additional information about a volume which it is assigned to. This information can range from 'Moun... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Property"
---

# SoftLayer_Network_Storage_Property
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Property' >Datatype</a></li>
    </ul>
</div>

## Description 
A property provides additional information about a volume which it is assigned to. This information can range from "Mountable" flags to utilized snapshot space. 





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
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The date a property was created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The date a property was last modified; </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#value" name=value>value</a>
            </span>
            <div class='views-field-body'>The value of a property. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#volumeId" name=volumeId>volumeId</a>
            </span>
            <div class='views-field-body'>The volume id which a property is associated with. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#type" name=type>type</a>
            </span>
            <div class='views-field-body'>The type provides a standardized definition for a property. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Storage_Property_Type'>SoftLayer_Network_Storage_Property_Type </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#volume" name=volume>volume</a>
            </span>
            <div class='views-field-body'>The associated volume for a property. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>



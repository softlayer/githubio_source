---
title: "SoftLayer_Hardware_Component_Attribute"
description: "The SoftLayer_Hardware_Component_Attribute data type contains general information relating to a single hardware setting... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Attribute"
---

# SoftLayer_Hardware_Component_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component_Attribute data type contains general information relating to a single hardware setting or attribute for a component model. For Example: A RAID controller may be setup for many different RAID configurations.  A RAID controller with a configuration of RAID-1 will have a single attribute for this RAID setting. 
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
            <span class='views-field-title'><a href="#hardwareComponentAttributeTypeId" name=hardwareComponentAttributeTypeId>hardwareComponentAttributeTypeId</a></span>
            <div class='views-field-body'>A hardware component attribute's associated [[SoftLayer_Hardware_Component_Attribute_Type|type]] Id. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponentId" name=hardwareComponentId>hardwareComponentId</a></span>
            <div class='views-field-body'>A hardware component attribute's associated [[SoftLayer_Hardware_Component|hardware component]] Id. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#value" name=value>value</a></span>
            <div class='views-field-body'>A hardware component attribute's value.  A value can have many different values depending on the attributes [[SoftLayer_Hardware_Component_Attribute_Type|type]]. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponent" name=hardwareComponent>hardwareComponent</a></span>
            <div class='views-field-body'>A hardware component attribute's associated [[SoftLayer_Hardware_Component|Hardware Component]]. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponentAttributeType" name=hardwareComponentAttributeType>hardwareComponentAttributeType</a></span>
            <div class='views-field-body'>A hardware component attribute's associated [[SoftLayer_Hardware_Component_Attribute_Type|type]]. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Attribute_Type'>SoftLayer_Hardware_Component_Attribute_Type </a></p></div>
        </div>
            </div>
</div>



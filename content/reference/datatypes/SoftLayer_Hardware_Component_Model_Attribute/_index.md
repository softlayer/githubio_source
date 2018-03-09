---
title: "SoftLayer_Hardware_Component_Model_Attribute"
description: "The SoftLayer_Hardware_Component__Model_Attribute data type contains general information relating to a single hardware s... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Model_Attribute"
---

# SoftLayer_Hardware_Component_Model_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component__Model_Attribute data type contains general information relating to a single hardware setting or attribute for a component model. 





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
                <a href="#attributeTypeId" name=attributeTypeId>attributeTypeId</a>
            </span>
            <div class='views-field-body'>A hardware component model attribute's associated [[SoftLayer_Hardware_Component_Model_Attribute_Type|type]] Id. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareComponentModelId" name=hardwareComponentModelId>hardwareComponentModelId</a>
            </span>
            <div class='views-field-body'>A hardware component model attribute's associated [[SoftLayer_Hardware_Component_Model|hardware component model]] Id. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#value" name=value>value</a>
            </span>
            <div class='views-field-body'>A hardware component model attribute's value.  A value can have many different values depending on the attributes [[SoftLayer_Hardware_Component_Model_Attribute_Type|type]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareComponent" name=hardwareComponent>hardwareComponent</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareComponentAttributeType" name=hardwareComponentAttributeType>hardwareComponentAttributeType</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Attribute_Type'>SoftLayer_Hardware_Component_Model_Attribute_Type </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>



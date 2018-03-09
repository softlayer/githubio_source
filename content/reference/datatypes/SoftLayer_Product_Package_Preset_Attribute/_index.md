---
title: "SoftLayer_Product_Package_Preset_Attribute"
description: "Package preset attributes contain supplementary information for a package preset."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Preset_Attribute"
---

# SoftLayer_Product_Package_Preset_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Preset_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
Package preset attributes contain supplementary information for a package preset. 



### seeAlso

* [SoftLayer_Product_Package_Preset](/reference/services/SoftLayer_Product_Package_Preset )


* [SoftLayer_Product_Package_Preset_Attribute_Type](/reference/datatypes/SoftLayer_Product_Package_Preset_Attribute_Type )




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
            <div class='views-field-body'>The internal identifier of the type of attribute that a pacakge preset attribute belongs to.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A package preset attribute's internal identifier.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#presetId" name=presetId>presetId</a>
            </span>
            <div class='views-field-body'>The internal identifier of the package preset an attribute belongs to.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#value" name=value>value</a>
            </span>
            <div class='views-field-body'>A package preset's attribute value.  </div>
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
                <a href="#attributeType" name=attributeType>attributeType</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package_Preset_Attribute_Type'>SoftLayer_Product_Package_Preset_Attribute_Type </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#preset" name=preset>preset</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>



---
title: "SoftLayer_Product_Item_Rule_Resource_Permission"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Rule_Resource_Permission"
---

# SoftLayer_Product_Item_Rule_Resource_Permission
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource_Permission' >Datatype</a></li>
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
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resourceTableId" name=resourceTableId>resourceTableId</a></span>
            <div class='views-field-body'>The unique identifier of the resource. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ruleId" name=ruleId>ruleId</a></span>
            <div class='views-field-body'>The unique identifier of the rule this resource is included in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resource" name=resource>resource</a></span>
            <div class='views-field-body'>A user permission that the associated rule applies to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission'>SoftLayer_User_Customer_CustomerPermission_Permission </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#rule" name=rule>rule</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Rule'>SoftLayer_Product_Item_Rule </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>



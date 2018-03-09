---
title: "SoftLayer_Product_Item_Attribute"
description: "The [[SoftLayer_Product_Item_Attribute]] data type allows us to describe a [[SoftLayer_Product_Item]] by attaching speci... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Attribute"
---

# SoftLayer_Product_Item_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
The [[SoftLayer_Product_Item_Attribute]] data type allows us to describe a [[SoftLayer_Product_Item]] by attaching specific attributes, which may dictate how it interacts with other products and services. Most, if not all, of these attributes are geared towards internal usage, so customers should rarely be concerned with them. 





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
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>This is the primary key value for the product attribute. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemAttributeTypeId" name=itemAttributeTypeId>itemAttributeTypeId</a>
            </span>
            <div class='views-field-body'>This is a foreign key value for the [[SoftLayer_Product_Item_Attribute_Type]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemId" name=itemId>itemId</a>
            </span>
            <div class='views-field-body'>This is a foreign key value for the [[SoftLayer_Product_Item]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#value" name=value>value</a>
            </span>
            <div class='views-field-body'>This is the value for the attribute. </div>
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
            <div class='views-field-body'>This represents the attribute type of this product attribute. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Attribute_Type'>SoftLayer_Product_Item_Attribute_Type </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#attributeTypeKeyName" name=attributeTypeKeyName>attributeTypeKeyName</a>
            </span>
            <div class='views-field-body'>This represents the attribute type's key name of this product attribute. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#item" name=item>item</a>
            </span>
            <div class='views-field-body'>This represents the product that an attribute is tied to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>



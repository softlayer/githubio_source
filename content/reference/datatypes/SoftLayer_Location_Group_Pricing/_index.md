---
title: "SoftLayer_Location_Group_Pricing"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Group_Pricing"
---

# SoftLayer_Location_Group_Pricing
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Group_Pricing' >Datatype</a></li>
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
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationGroupTypeId" name=locationGroupTypeId>locationGroupTypeId</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#securityLevelId" name=securityLevelId>securityLevelId</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationGroupType" name=locationGroupType>locationGroupType</a></span>
            <div class='views-field-body'>The type for this location group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location_Group_Type'>SoftLayer_Location_Group_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locations" name=locations>locations</a></span>
            <div class='views-field-body'>The locations that this pricing location group is applicable for. This limits the locations that the prices referenced by this pricing location group can be used with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#prices" name=prices>prices</a></span>
            <div class='views-field-body'>The prices that this pricing location group limits. All of these prices will only be available in the locations defined by this pricing location group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationCount" name=locationCount>locationCount</a></span>
            <div class='views-field-body'>A count of the locations that this pricing location group is applicable for. This limits the locations that the prices referenced by this pricing location group can be used with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#priceCount" name=priceCount>priceCount</a></span>
            <div class='views-field-body'>A count of the prices that this pricing location group limits. All of these prices will only be available in the locations defined by this pricing location group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>



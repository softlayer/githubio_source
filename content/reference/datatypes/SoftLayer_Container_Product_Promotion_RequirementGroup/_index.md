---
title: "SoftLayer_Container_Product_Promotion_RequirementGroup"
description: "The SoftLayer_Container_Product_Promotion_RequirementGroup data type contains the required options that must be present... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Product_Promotion_RequirementGroup"
---

# SoftLayer_Container_Product_Promotion_RequirementGroup
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Product_Promotion_RequirementGroup' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Product_Promotion_RequirementGroup data type contains the required options that must be present on an order for the promotion to be applied. At least one of the categories, presets, or prices must be on the order. 





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
                <a href="#categories" name=categories>categories</a>
            </span>
            <div class='views-field-body'>The category options to choose from for this requirement group  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#presets" name=presets>presets</a>
            </span>
            <div class='views-field-body'>The preset options to choose from for this requirement group  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#prices" name=prices>prices</a>
            </span>
            <div class='views-field-body'>The price options to choose from for this requirement group  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a></p>
            </div>
        </div>
            </div>
    </div>



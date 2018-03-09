---
title: "SoftLayer_Product_Package_Order_Configuration"
description: "This datatype describes the item categories that are required for each package to be ordered. For instance, for package... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Order_Configuration"
---

# SoftLayer_Product_Package_Order_Configuration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Order_Configuration' >Datatype</a></li>
    </ul>
</div>

## Description 
This datatype describes the item categories that are required for each package to be ordered. For instance, for package 2, there will be many required categories. When submitting an order for a server, there must be at most 1 price for each category whose "isRequired" is set. Examples of required categories: - server - ram - bandwidth - disk0 

There are others, but these are the main ones. For each required category, a SoftLayer_Product_Item_Price must be chosen that is valid for the package. 




### associatedMethods

*  [SoftLayer_Product_Package_Item_Prices::getObject](/reference/services/SoftLayer_Product_Package_Item_Prices/getObject )
*  [SoftLayer_Product_Package_Items::getObject](/reference/services/SoftLayer_Product_Package_Items/getObject )





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
                <a href="#errorMessage" name=errorMessage>errorMessage</a>
            </span>
            <div class='views-field-body'>The error message displayed if the submitted order does not contain this item category, if it is required. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier for this object. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#isRequired" name=isRequired>isRequired</a>
            </span>
            <div class='views-field-body'>This is a flag which tells SoftLayer_Product_Order::verifyOrder() whether or not this category is required. If this is set, then the order submitted must contain a SoftLayer_Product_Item_Price with this category as part of the order.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemCategoryId" name=itemCategoryId>itemCategoryId</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Product_Item_Category. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#orderStepId" name=orderStepId>orderStepId</a>
            </span>
            <div class='views-field-body'>The order step ID for this particular option in the package. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#packageId" name=packageId>packageId</a>
            </span>
            <div class='views-field-body'>The PackageId tied to this instance. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sort" name=sort>sort</a>
            </span>
            <div class='views-field-body'>This is an integer used to show the order in which each item Category should be displayed. This is merely the suggested order. </div>
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
                <a href="#itemCategory" name=itemCategory>itemCategory</a>
            </span>
            <div class='views-field-body'>The item category for this configuration instance. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#package" name=package>package</a>
            </span>
            <div class='views-field-body'>The package to which this instance belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#step" name=step>step</a>
            </span>
            <div class='views-field-body'>The step to which this instance belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step'>SoftLayer_Product_Package_Order_Step </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>



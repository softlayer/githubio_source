---
title: "SoftLayer_Product_Item_Bundles"
description: "The SoftLayer_Product_Item_Bundles contains item to price cross references Relates a category, price and item to a bundl... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Bundles"
---

# SoftLayer_Product_Item_Bundles
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Bundles' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Product_Item_Bundles contains item to price cross references Relates a category, price and item to a bundle.  Match bundle ids to see all items and prices in a particular bundle. 



### seeAlso

* [SoftLayer_Product_Item](/reference/datatypes/SoftLayer_Product_Item )


* [SoftLayer_Product_Item_Price](/reference/services/SoftLayer_Product_Item_Price )


* [SoftLayer_Product_Item_Category](/reference/services/SoftLayer_Product_Item_Category )




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
                <a href="#bundleItemId" name=bundleItemId>bundleItemId</a>
            </span>
            <div class='views-field-body'>Identifier for bundle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>Identifier for record. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemPriceId" name=itemPriceId>itemPriceId</a>
            </span>
            <div class='views-field-body'>Identifier for price. </div>
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
                <a href="#bundleItem" name=bundleItem>bundleItem</a>
            </span>
            <div class='views-field-body'>Item in bundle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#category" name=category>category</a>
            </span>
            <div class='views-field-body'>Category bundle falls in. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemPrice" name=itemPrice>itemPrice</a>
            </span>
            <div class='views-field-body'>Price of item in bundle </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>



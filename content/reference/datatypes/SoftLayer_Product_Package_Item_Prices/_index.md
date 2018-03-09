---
title: "SoftLayer_Product_Package_Item_Prices"
description: "The SoftLayer_Product_Package_Item_Prices contains price to package cross references Relates a category, price and item... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Item_Prices"
---

# SoftLayer_Product_Package_Item_Prices
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Item_Prices' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Product_Package_Item_Prices contains price to package cross references Relates a category, price and item to a bundle.  Match bundle ids to see all items and prices in a particular bundle. 



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
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier for SoftLayer_Product_Package_Item_Price. This is only needed as a reference. The important data is the itemPriceId property.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemPriceId" name=itemPriceId>itemPriceId</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Product_Item_Price id. This value is to be used when placing orders. To get more information about this item price, go from the item price to the item description  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#packageId" name=packageId>packageId</a>
            </span>
            <div class='views-field-body'>The Package ID to which this price reference belongs </div>
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
                <a href="#itemPrice" name=itemPrice>itemPrice</a>
            </span>
            <div class='views-field-body'>The item price to which this object belongs. The item price has details regarding cost for the item it belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#package" name=package>package</a>
            </span>
            <div class='views-field-body'>The package to which this object belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>



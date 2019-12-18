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

## Local
-----
[id]: #id
#### [id]
The unique identifier for SoftLayer_Product_Package_Item_Price. This is only needed as a reference. The important data is the itemPriceId property.   
<span class="type-label">Type: </span>**integer**

-----
[itemPriceId]: #itempriceid
#### [itemPriceId]
The SoftLayer_Product_Item_Price id. This value is to be used when placing orders. To get more information about this item price, go from the item price to the item description   
<span class="type-label">Type: </span>**integer**

-----
[packageId]: #packageid
#### [packageId]
The Package ID to which this price reference belongs  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[itemPrice]: #itemprice
#### [itemPrice]
The item price to which this object belongs. The item price has details regarding cost for the item it belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>**

-----
[package]: #package
#### [package]
The package to which this object belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**


## Count
</div>



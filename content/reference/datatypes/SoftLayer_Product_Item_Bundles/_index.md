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




<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[bundleItemId]: #bundleitemid
#### [bundleItemId]
Identifier for bundle.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Identifier for record.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[itemPriceId]: #itempriceid
#### [itemPriceId]
Identifier for price.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[bundleItem]: #bundleitem
#### [bundleItem]
Item in bundle.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>
<div class="prop-row">

-----
[category]: #category
#### [category]
Category bundle falls in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>**


</div>
<div class="prop-row">

-----
[itemPrice]: #itemprice
#### [itemPrice]
Price of item in bundle  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>**


</div>

## Count
</div>



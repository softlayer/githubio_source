---
title: "SoftLayer_Product_Catalog_Item_Price"
description: "The SoftLayer_Product_Catalog_Item_Price type assigns an Item Price to a Catalog. This relation defines the composition... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Catalog_Item_Price"
---

# SoftLayer_Product_Catalog_Item_Price
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Catalog_Item_Price' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Product_Catalog_Item_Price type assigns an Item Price to a Catalog. This relation defines the composition of Item Prices in a Catalog. 





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
[catalogId]: #catalogid
#### [catalogId]
The id of the Catalog the Item Price is part of.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The time the Item Price was defined in the Catalog  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The time the Item Price was changed for the Catalog  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[priceId]: #priceid
#### [priceId]
The id of the Item Price that is part of the Catalog.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[catalog]: #catalog
#### [catalog]
Catalog being assigned  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Catalog'>SoftLayer_Product_Catalog </a>**  



</div>
<div class="prop-row">

-----
[price]: #price
#### [price]
Price being assigned  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>**  



</div>

## Count
</div>



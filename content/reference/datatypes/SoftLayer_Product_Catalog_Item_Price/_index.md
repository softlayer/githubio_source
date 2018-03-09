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
                <a href="#catalogId" name=catalogId>catalogId</a>
            </span>
            <div class='views-field-body'>The id of the Catalog the Item Price is part of. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The time the Item Price was defined in the Catalog </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The time the Item Price was changed for the Catalog </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#priceId" name=priceId>priceId</a>
            </span>
            <div class='views-field-body'>The id of the Item Price that is part of the Catalog. </div>
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
                <a href="#catalog" name=catalog>catalog</a>
            </span>
            <div class='views-field-body'>Catalog being assigned </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Catalog'>SoftLayer_Product_Catalog </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#price" name=price>price</a>
            </span>
            <div class='views-field-body'>Price being assigned </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>



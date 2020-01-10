---
title: "SoftLayer_Product_Package_Item_Category_Group"
description: "This class is used to organize categories for a service offering. A service offering (usually) contains multiple categor... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Item_Category_Group"
---

# SoftLayer_Product_Package_Item_Category_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Item_Category_Group' >Datatype</a></li>
    </ul>
</div>

## Description 
This class is used to organize categories for a service offering. A service offering (usually) contains multiple categories (e.g., server, os, disk0, ram). This class allows us to organize the prices into related item category groups. 





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
[itemCategoryId]: #itemcategoryid
#### [itemCategoryId]
The item category id associated with this group.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[packageId]: #packageid
#### [packageId]
The service offering id associated with this group.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[sort]: #sort
#### [sort]
The sort value for this group.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[title]: #title
#### [title]
An optional title associated with this group. E.g., for operating systems, this will be the manufacturer.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[category]: #category
#### [category]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>**


</div>
<div class="prop-row">

-----
[package]: #package
#### [package]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**


</div>
<div class="prop-row">

-----
[prices]: #prices
#### [prices]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**


</div>

## Count
<div class="prop-row">

-----
[priceCount]: #pricecount
#### [priceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>



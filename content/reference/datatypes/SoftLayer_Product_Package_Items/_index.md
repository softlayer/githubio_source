---
title: "SoftLayer_Product_Package_Items"
description: "This data type is a cross-reference between the SoftLayer_Product_Package and the SoftLayer_Product_Item(s) that belong... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Items"
---

# SoftLayer_Product_Package_Items
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Items' >Datatype</a></li>
    </ul>
</div>

## Description 
This data type is a cross-reference between the SoftLayer_Product_Package and the SoftLayer_Product_Item(s) that belong in the SoftLayer_Product_Package. 





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
[id]: #id
#### [id]
The unique identifier for this object. It is not used anywhere but in this object.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[itemId]: #itemid
#### [itemId]
The SoftLayer_Product_Item id to which this instance of the object belongs.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[packageId]: #packageid
#### [packageId]
The SoftLayer_Product_Package id to which this instance of the object belongs.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[item]: #item
#### [item]
The item to which this object belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>
<div class="prop-row">

-----
[package]: #package
#### [package]
The package to which this object belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**


</div>

## Count
</div>



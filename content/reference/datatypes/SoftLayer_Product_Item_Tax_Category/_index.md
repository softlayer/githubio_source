---
title: "SoftLayer_Product_Item_Tax_Category"
description: "The SoftLayer_Product_Item_Tax_Category data type contains the tax categories that are associated with products."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Tax_Category"
---

# SoftLayer_Product_Item_Tax_Category
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Tax_Category' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Product_Item_Tax_Category data type contains the tax categories that are associated with products. 





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
An internal identifier for each tax category.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
The key name of the tax category.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name of the tax category.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[statusFlag]: #statusflag
#### [statusFlag]
The status of the tax category.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[items]: #items
#### [items]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[itemCount]: #itemcount
#### [itemCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>



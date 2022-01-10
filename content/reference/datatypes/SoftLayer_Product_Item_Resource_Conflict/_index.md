---
title: "SoftLayer_Product_Item_Resource_Conflict"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Resource_Conflict"
---

# SoftLayer_Product_Item_Resource_Conflict
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict' >Datatype</a></li>
    </ul>
</div>

## Description 








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
[itemId]: #itemid
#### [itemId]
The unique identifier of the item that contains the conflict.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[message]: #message
#### [message]
An optional conflict message.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[packageId]: #packageid
#### [packageId]
The unique identifier of the service offering that is associated with the conflict.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
The unique identifier of the conflicting type.  
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
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**  



</div>
<div class="prop-row">

-----
[package]: #package
#### [package]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**  



</div>

## Count
</div>



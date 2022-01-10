---
title: "SoftLayer_Product_Item_Attribute"
description: "The [SoftLayer_Product_Item_Attribute]({{<ref 'reference/datatypes/SoftLayer_Product_Item_Attribute'>}}) data type allow... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Attribute"
---

# SoftLayer_Product_Item_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 


The [SoftLayer_Product_Item_Attribute]({{<ref "reference/datatypes/SoftLayer_Product_Item_Attribute">}}) data type allows us to describe a [SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}}) by attaching specific attributes, which may dictate how it interacts with other products and services. Most, if not all, of these attributes are geared towards internal usage, so customers should rarely be concerned with them. 





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
This is the primary key value for the product attribute.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[itemAttributeTypeId]: #itemattributetypeid
#### [itemAttributeTypeId]
This is a foreign key value for the [SoftLayer_Product_Item_Attribute_Type]({{<ref "reference/datatypes/SoftLayer_Product_Item_Attribute_Type">}}).  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[itemId]: #itemid
#### [itemId]
This is a foreign key value for the [SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}}).  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[value]: #value
#### [value]
This is the value for the attribute.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[attributeType]: #attributetype
#### [attributeType]
This represents the attribute type of this product attribute.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Attribute_Type'>SoftLayer_Product_Item_Attribute_Type </a>**  



</div>
<div class="prop-row">

-----
[attributeTypeKeyName]: #attributetypekeyname
#### [attributeTypeKeyName]
This represents the attribute type's key name of this product attribute.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[item]: #item
#### [item]
This represents the product that an attribute is tied to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**  



</div>

## Count
</div>



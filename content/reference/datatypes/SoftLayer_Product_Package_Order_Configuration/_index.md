---
title: "SoftLayer_Product_Package_Order_Configuration"
description: "This datatype describes the item categories that are required for each package to be ordered. For instance, for package... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Order_Configuration"
---

# SoftLayer_Product_Package_Order_Configuration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Order_Configuration' >Datatype</a></li>
    </ul>
</div>

## Description 
This datatype describes the item categories that are required for each package to be ordered. For instance, for package 2, there will be many required categories. When submitting an order for a server, there must be at most 1 price for each category whose "isRequired" is set. Examples of required categories: - server - ram - bandwidth - disk0 

There are others, but these are the main ones. For each required category, a SoftLayer_Product_Item_Price must be chosen that is valid for the package. 




### associatedMethods

*  [SoftLayer_Product_Package_Item_Prices::getObject](/reference/services/SoftLayer_Product_Package_Item_Prices/getObject )
*  [SoftLayer_Product_Package_Items::getObject](/reference/services/SoftLayer_Product_Package_Items/getObject )





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
[bundledFlag]: #bundledflag
#### [bundledFlag]
Signifies that selections associated with the configuration are automatically provided by being bundled to another configurations selection. The actual bundling is on the product.   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[errorMessage]: #errormessage
#### [errorMessage]
The error message displayed if the submitted order does not contain this item category, if it is required.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique identifier for this object.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[isRequired]: #isrequired
#### [isRequired]
This is a flag which tells SoftLayer_Product_Order::verifyOrder() whether or not this category is required. If this is set, then the order submitted must contain a SoftLayer_Product_Item_Price with this category as part of the order.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[itemCategoryId]: #itemcategoryid
#### [itemCategoryId]
The SoftLayer_Product_Item_Category.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[orderStepId]: #orderstepid
#### [orderStepId]
The order step ID for this particular option in the package.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[packageId]: #packageid
#### [packageId]
The PackageId tied to this instance.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[sort]: #sort
#### [sort]
This is an integer used to show the order in which each item Category should be displayed. This is merely the suggested order.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[itemCategory]: #itemcategory
#### [itemCategory]
The item category for this configuration instance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>**


</div>
<div class="prop-row">

-----
[package]: #package
#### [package]
The package to which this instance belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**


</div>
<div class="prop-row">

-----
[step]: #step
#### [step]
The step to which this instance belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step'>SoftLayer_Product_Package_Order_Step </a>**


</div>

## Count
</div>



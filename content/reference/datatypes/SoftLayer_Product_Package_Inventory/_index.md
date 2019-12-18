---
title: "SoftLayer_Product_Package_Inventory"
description: "This is deprecated."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Inventory"
---

# SoftLayer_Product_Package_Inventory
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Inventory' >Datatype</a></li>
    </ul>
</div>

## Description 
This is deprecated. 





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
[availableInventoryCount]: #availableinventorycount
#### [availableInventoryCount]
DEPRECATED. The number of units available for purchase in inventory for a single item in a single datacenter.   
<span class="type-label">Type: </span>**integer**

-----
[itemId]: #itemid
#### [itemId]
DEPRECATED. The unique identifier of the product item that an inventory record is associated with.   
<span class="type-label">Type: </span>**integer**

-----
[locationId]: #locationid
#### [locationId]
DEPRECATED. The unique identifier of the datacenter that an inventory record is located in.   
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
DEPRECATED. The date that an inventory record was last updated.   
<span class="type-label">Type: </span>**dateTime**

-----
[overstockFlag]: #overstockflag
#### [overstockFlag]
DEPRECATED. Whether an inventory record is marked as "overstock".   
<span class="type-label">Type: </span>**integer**

-----
[packageId]: #packageid
#### [packageId]
DEPRECATED. The unique identifier of the product package that an inventory record is associated with.   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[item]: #item
#### [item]
The product package item that is associated with an inventory record.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**

-----
[location]: #location
#### [location]
The datacenter that an inventory record is located in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[package]: #package
#### [package]
The product package that is associated with an inventory record.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**


## Count
</div>



---
title: "SoftLayer_Account_Shipment_Item"
description: "The SoftLayer_Account_Shipment_Item data type contains information relating to a shipment's item. Basic information such... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Shipment_Item"
---

# SoftLayer_Account_Shipment_Item
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Shipment_Item' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Shipment_Item' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Account_Shipment_Item data type contains information relating to a shipment's item. Basic information such as addresses, the shipment courier, and any tracking information for as shipment is accessible with this data type. 





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
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
The description of the shipping item.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique id of the shipping item.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[packageId]: #packageid
#### [packageId]
The package id of the shipping item.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[shipmentId]: #shipmentid
#### [shipmentId]
The shipment id of the shipping item.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[shipmentItemId]: #shipmentitemid
#### [shipmentItemId]
The item id of the shipping item.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[shipmentItemTypeId]: #shipmentitemtypeid
#### [shipmentItemTypeId]
The item type id of the shipping item.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[shipment]: #shipment
#### [shipment]
The shipment to which this item belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Shipment'>SoftLayer_Account_Shipment </a>**  



</div>
<div class="prop-row">

-----
[shipmentItemType]: #shipmentitemtype
#### [shipmentItemType]
The type of this shipment item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Shipment_Item_Type'>SoftLayer_Account_Shipment_Item_Type </a>**  



</div>

## Count
</div>



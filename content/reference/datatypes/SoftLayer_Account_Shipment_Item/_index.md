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
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Shipment_Item' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Account_Shipment_Item data type contains information relating to a shipment's item. Basic information such as addresses, the shipment courier, and any tracking information for as shipment is accessible with this data type. 





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
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>The description of the shipping item. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique id of the shipping item. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#packageId" name=packageId>packageId</a></span>
            <div class='views-field-body'>The package id of the shipping item. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#shipmentId" name=shipmentId>shipmentId</a></span>
            <div class='views-field-body'>The shipment id of the shipping item. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#shipmentItemId" name=shipmentItemId>shipmentItemId</a></span>
            <div class='views-field-body'>The item id of the shipping item. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#shipmentItemTypeId" name=shipmentItemTypeId>shipmentItemTypeId</a></span>
            <div class='views-field-body'>The item type id of the shipping item. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#shipment" name=shipment>shipment</a></span>
            <div class='views-field-body'>The shipment to which this item belongs. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account_Shipment'>SoftLayer_Account_Shipment </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#shipmentItemType" name=shipmentItemType>shipmentItemType</a></span>
            <div class='views-field-body'>The type of this shipment item. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account_Shipment_Item_Type'>SoftLayer_Account_Shipment_Item_Type </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>



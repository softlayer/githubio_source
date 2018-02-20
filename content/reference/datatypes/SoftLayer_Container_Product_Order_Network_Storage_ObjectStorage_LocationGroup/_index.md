---
title: "SoftLayer_Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup"
description: "This class is used to contain a location group and its associated active usage rate prices for object storage ordering."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup"
---

# SoftLayer_Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup' >Datatype</a></li>
    </ul>
</div>

## Description 
This class is used to contain a location group and its associated active usage rate prices for object storage ordering. 
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
            <span class='views-field-title'><a href="#clusterGeolocationType" name=clusterGeolocationType>clusterGeolocationType</a></span>
            <div class='views-field-body'>The datacenter location where object storage is available. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationGroup" name=locationGroup>locationGroup</a></span>
            <div class='views-field-body'>The datacenter location where object storage is available. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location_Group'>SoftLayer_Location_Group </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#usageRatePrices" name=usageRatePrices>usageRatePrices</a></span>
            <div class='views-field-body'>The collection of active usage rate item prices. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a></p></div>
        </div>
            </div>
    </div>



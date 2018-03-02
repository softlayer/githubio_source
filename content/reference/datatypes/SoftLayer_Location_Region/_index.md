---
title: "SoftLayer_Location_Region"
description: "A region is made up of a keyname and a description of that region. A region keyname can be used as part of an order. Che... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Region"
---

# SoftLayer_Location_Region
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Region' >Datatype</a></li>
    </ul>
</div>

## Description 
A region is made up of a keyname and a description of that region. A region keyname can be used as part of an order. Check the SoftLayer_Product_Order service for more details. 


### associatedMethods

*  [SoftLayer_Product_Order::verifyOrder](/reference/services/SoftLayer_Product_Order/verifyOrder )
*  [SoftLayer_Product_Order::placeOrder](/reference/services/SoftLayer_Product_Order/placeOrder )





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
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>A short description of a region's name. This description is seen on the order forms.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keyname" name=keyname>keyname</a></span>
            <div class='views-field-body'>A unique key name for a region. Provided for easy debugging. This is to be sent in with an order.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sortOrder" name=sortOrder>sortOrder</a></span>
            <div class='views-field-body'>An integer representing the order in which this element is displayed. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#location" name=location>location</a></span>
            <div class='views-field-body'>Each region can have many locations tied to it. However, this is the location we currently provision to for a region. This location is the current valid location for a region. (Deprecated, use 'locations') </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location_Region_Location'>SoftLayer_Location_Region_Location </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locations" name=locations>locations</a></span>
            <div class='views-field-body'>The locations (like datacenters or PoPs) in this region. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location_Region_Location'>SoftLayer_Location_Region_Location[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationCount" name=locationCount>locationCount</a></span>
            <div class='views-field-body'>A count of the locations (like datacenters or PoPs) in this region. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>



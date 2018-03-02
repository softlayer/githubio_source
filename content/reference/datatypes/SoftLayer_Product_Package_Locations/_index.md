---
title: "SoftLayer_Product_Package_Locations"
description: "Most packages are available in many locations. This object describes that availability for each package."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Locations"
---

# SoftLayer_Product_Package_Locations
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Locations' >Datatype</a></li>
    </ul>
</div>

## Description 
Most packages are available in many locations. This object describes that availability for each package. 





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
            <span class='views-field-title'><a href="#deliveryTimeInformation" name=deliveryTimeInformation>deliveryTimeInformation</a></span>
            <div class='views-field-body'>This describes the availability of the package tied to this location. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isAvailable" name=isAvailable>isAvailable</a></span>
            <div class='views-field-body'>A simple flag which describes whether or not this location is available for this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationId" name=locationId>locationId</a></span>
            <div class='views-field-body'>The location id tied to this object. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#packageId" name=packageId>packageId</a></span>
            <div class='views-field-body'>The SoftLayer_Product_Package ID tied to this object. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#location" name=location>location</a></span>
            <div class='views-field-body'>The location to which this object belongs. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#package" name=package>package</a></span>
            <div class='views-field-body'>The package to which this object belongs. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>



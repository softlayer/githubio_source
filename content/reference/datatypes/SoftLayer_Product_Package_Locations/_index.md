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
[deliveryTimeInformation]: #deliverytimeinformation
#### [deliveryTimeInformation]
This describes the availability of the package tied to this location.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[isAvailable]: #isavailable
#### [isAvailable]
A simple flag which describes whether or not this location is available for this package.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[locationId]: #locationid
#### [locationId]
The location id tied to this object.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[packageId]: #packageid
#### [packageId]
The SoftLayer_Product_Package ID tied to this object.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[location]: #location
#### [location]
The location to which this object belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[package]: #package
#### [package]
The package to which this object belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**


</div>

## Count
</div>



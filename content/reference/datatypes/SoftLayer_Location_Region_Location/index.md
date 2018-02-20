---
title: "SoftLayer_Location_Region_Location"
description: "The SoftLayer_Location_Region_Location is very specific to the location where services will actually be provisioned. Whe... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Region_Location"
---

# SoftLayer_Location_Region_Location
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Region_Location' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Location_Region_Location is very specific to the location where services will actually be provisioned. When accessed through a package, this location is the top priority location for a region. All new servers and services are provisioned at this location. When a server is ordered and a region is selected, this is the location within that region where the server will actually exist and have software/services installed. 
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
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#location" name=location>location</a></span>
            <div class='views-field-body'>The SoftLayer_Location tied to a region's location. This provides more information about the location, including specific datacenter information. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationPackageDetails" name=locationPackageDetails>locationPackageDetails</a></span>
            <div class='views-field-body'>A region's location also has delivery information as well as other information to be determined. For now, availability is provided and could weigh into the decision as to where to decide to have a server provisioned.' </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Locations'>SoftLayer_Product_Package_Locations[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#region" name=region>region</a></span>
            <div class='views-field-body'>The region to which this location belongs. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location_Region'>SoftLayer_Location_Region </a></p></div>
        </div>
            </div>
</div>



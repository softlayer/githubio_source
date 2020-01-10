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
[locationId]: #locationid
#### [locationId]
  
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
The SoftLayer_Location tied to a region's location. This provides more information about the location, including specific datacenter information.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[locationPackageDetails]: #locationpackagedetails
#### [locationPackageDetails]
A region's location also has delivery information as well as other information to be determined. For now, availability is provided and could weigh into the decision as to where to decide to have a server provisioned.'  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Locations'>SoftLayer_Product_Package_Locations[] </a>**


</div>
<div class="prop-row">

-----
[region]: #region
#### [region]
The region to which this location belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Region'>SoftLayer_Location_Region </a>**


</div>

## Count
<div class="prop-row">

-----
[locationPackageDetailCount]: #locationpackagedetailcount
#### [locationPackageDetailCount]
A count of a region's location also has delivery information as well as other information to be determined. For now, availability is provided and could weigh into the decision as to where to decide to have a server provisioned.'   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>



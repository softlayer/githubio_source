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
[description]: #description
#### [description]
A short description of a region's name. This description is seen on the order forms.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[keyname]: #keyname
#### [keyname]
A unique key name for a region. Provided for easy debugging. This is to be sent in with an order.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[sortOrder]: #sortorder
#### [sortOrder]
An integer representing the order in which this element is displayed.  
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
Each region can have many locations tied to it. However, this is the location we currently provision to for a region. This location is the current valid location for a region. (Deprecated, use 'locations')  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Region_Location'>SoftLayer_Location_Region_Location </a>**


</div>
<div class="prop-row">

-----
[locations]: #locations
#### [locations]
The locations (like datacenters or PoPs) in this region.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Region_Location'>SoftLayer_Location_Region_Location[] </a>**


</div>

## Count
<div class="prop-row">

-----
[locationCount]: #locationcount
#### [locationCount]
A count of the locations (like datacenters or PoPs) in this region.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>



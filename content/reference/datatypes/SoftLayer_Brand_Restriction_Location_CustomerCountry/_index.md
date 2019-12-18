---
title: "SoftLayer_Brand_Restriction_Location_CustomerCountry"
description: "The [SoftLayer_Brand_Restriction_Location_CustomerCountry]({{<ref 'reference/datatypes/SoftLayer_Brand_Restriction_Locat... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand_Restriction_Location_CustomerCountry"
---

# SoftLayer_Brand_Restriction_Location_CustomerCountry
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Brand_Restriction_Location_CustomerCountry' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Brand_Restriction_Location_CustomerCountry' >Datatype</a></li>
    </ul>
</div>

## Description 
The [SoftLayer_Brand_Restriction_Location_CustomerCountry]({{<ref "reference/datatypes/SoftLayer_Brand_Restriction_Location_CustomerCountry">}}) data type defines the relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on the SoftLayer US brand for customers that live in Great Britain. 





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
[brandId]: #brandid
#### [brandId]
The brand associated with customer's account.  
<span class="type-label">Type: </span>**integer**

-----
[customerCountryCode]: #customercountrycode
#### [customerCountryCode]
country code associated with customer's account.  
<span class="type-label">Type: </span>**string**

-----
[locationId]: #locationid
#### [locationId]
The id for datacenter location.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[brand]: #brand
#### [brand]
This references the brand that has a brand-location-country restriction setup.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a>**

-----
[location]: #location
#### [location]
This references the datacenter that has a brand-location-country restriction setup. For example, if a datacenter is listed with a restriction for Canada, a Canadian customer may not be eligible to order services at that location.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


## Count
</div>



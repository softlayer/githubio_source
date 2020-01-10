---
title: "SoftLayer_Brand_Restriction_Location_CustomerCountry"
description: "The [SoftLayer_Brand_Restriction_Location_CustomerCountry]({{<ref 'reference/datatypes/SoftLayer_Brand_Restriction_Locat... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
The [SoftLayer_Brand_Restriction_Location_CustomerCountry]({{<ref "reference/datatypes/SoftLayer_Brand_Restriction_Location_CustomerCountry">}}) service defines the relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on the SoftLayer US brand for customers that live in Great Britain. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [getAllObjects](/reference/services/SoftLayer_Brand_Restriction_Location_CustomerCountry/getAllObjects)

</div>

<div class="method-row">

#### [getBrand](/reference/services/SoftLayer_Brand_Restriction_Location_CustomerCountry/getBrand)
Retrieve this references the brand that has a brand-location-country restriction setup.
</div>

<div class="method-row">

#### [getLocation](/reference/services/SoftLayer_Brand_Restriction_Location_CustomerCountry/getLocation)
Retrieve this references the datacenter that has a brand-location-country restriction setup. For example, if a datacenter is listed with a restriction for Canada, a Canadian customer may not be eligible to order services at that location.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Brand_Restriction_Location_CustomerCountry/getObject)
Retrieve a SoftLayer_Brand_Restriction_Location_CustomerCountry record.
</div>
</div>

</div>


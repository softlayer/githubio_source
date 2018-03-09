---
title: "SoftLayer_Brand_Restriction_Location_CustomerCountry"
description: "The [[SoftLayer_Brand_Restriction_Location_CustomerCountry]] data type defines the relationship between brands, location... "
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
The [[SoftLayer_Brand_Restriction_Location_CustomerCountry]] data type defines the relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on the SoftLayer US brand for customers that live in Great Britain. 





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
            <span class='views-field-title'>
                <a href="#brandId" name=brandId>brandId</a>
            </span>
            <div class='views-field-body'>The brand associated with customer's account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#customerCountryCode" name=customerCountryCode>customerCountryCode</a>
            </span>
            <div class='views-field-body'>country code associated with customer's account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#locationId" name=locationId>locationId</a>
            </span>
            <div class='views-field-body'>The id for datacenter location. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#brand" name=brand>brand</a>
            </span>
            <div class='views-field-body'>This references the brand that has a brand-location-country restriction setup. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#location" name=location>location</a>
            </span>
            <div class='views-field-body'>This references the datacenter that has a brand-location-country restriction setup. For example, if a datacenter is listed with a restriction for Canada, a Canadian customer may not be eligible to order services at that location. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>



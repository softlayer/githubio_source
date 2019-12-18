---
title: "SoftLayer_Billing_Currency_Country"
description: "The SoftLayer_Billing_Currency_Country data type maps what currencies are valid for specific countries. US Dollars are v... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Currency_Country"
---

# SoftLayer_Billing_Currency_Country
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Currency_Country' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Currency_Country' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Billing_Currency_Country data type maps what currencies are valid for specific countries. US Dollars are valid from any country, but other currencies are only available to customers in certain countries. 





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
[countryId]: #countryid
#### [countryId]
A unique identifier for the related country.  
<span class="type-label">Type: </span>**integer**

-----
[currencyId]: #currencyid
#### [currencyId]
A unique identifier for the related currency.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A unique identifier for a map between a country and currency.  
<span class="type-label">Type: </span>**integer**

-----
[locale]: #locale
#### [locale]
The country currency locale.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>



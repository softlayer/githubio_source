---
title: "SoftLayer_Locale_Country"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Locale"
classes:
    - "SoftLayer_Locale_Country"
---

# SoftLayer_Locale_Country
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Locale_Country' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Locale_Country' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[isEuropeanUnionFlag]: #iseuropeanunionflag
#### [isEuropeanUnionFlag]
Binary flag denoting if this country is part of the European Union  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[isoCodeAlphaThree]: #isocodealphathree
#### [isoCodeAlphaThree]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[longName]: #longname
#### [longName]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[postalCodeFormat]: #postalcodeformat
#### [postalCodeFormat]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[postalCodeRequiredFlag]: #postalcoderequiredflag
#### [postalCodeRequiredFlag]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[shortName]: #shortname
#### [shortName]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[vatIdRegex]: #vatidregex
#### [vatIdRegex]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[vatIdRequiredFlag]: #vatidrequiredflag
#### [vatIdRequiredFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[states]: #states
#### [states]
States that belong to this country.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Locale_StateProvince'>SoftLayer_Locale_StateProvince[] </a>**


</div>

## Count
<div class="prop-row">

-----
[stateCount]: #statecount
#### [stateCount]
A count of states that belong to this country.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>



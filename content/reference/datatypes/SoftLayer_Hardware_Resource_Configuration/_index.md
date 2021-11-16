---
title: "SoftLayer_Hardware_Resource_Configuration"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Resource_Configuration"
---

# SoftLayer_Hardware_Resource_Configuration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Resource_Configuration' >Datatype</a></li>
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
[configurationTypeId]: #configurationtypeid
#### [configurationTypeId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[properties]: #properties
#### [properties]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Resource_Configuration_Property'>SoftLayer_Hardware_Resource_Configuration_Property[] </a>**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Resource_Configuration_Type'>SoftLayer_Hardware_Resource_Configuration_Type </a>**  



</div>

## Count
<div class="prop-row">

-----
[propertyCount]: #propertycount
#### [propertyCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>



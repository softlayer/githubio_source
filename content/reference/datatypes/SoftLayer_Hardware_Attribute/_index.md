---
title: "SoftLayer_Hardware_Attribute"
description: "The SoftLayer_Hardware_Attribute type contains general information for a hardware attribute. Hardware attributes can be... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Attribute"
---

# SoftLayer_Hardware_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Attribute type contains general information for a hardware attribute. Hardware attributes can be assigned to specific hardware objects to describe relatively arbitrary information. 





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
[hardwareAttributeTypeId]: #hardwareattributetypeid
#### [hardwareAttributeTypeId]
The unique identifier of a hardware attribute's type.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A hardware attribute's unique identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[value]: #value
#### [value]
A hardware attribute's value.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[hardwareAttributeType]: #hardwareattributetype
#### [hardwareAttributeType]
The type of hardware attribute that this represents.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Attribute_Type'>SoftLayer_Hardware_Attribute_Type </a>**


</div>

## Count
</div>



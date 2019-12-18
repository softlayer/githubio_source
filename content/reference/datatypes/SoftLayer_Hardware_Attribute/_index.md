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
[hardwareAttributeTypeId]: #hardwareattributetypeid
#### [hardwareAttributeTypeId]
The unique identifier of a hardware attribute's type.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A hardware attribute's unique identifier.  
<span class="type-label">Type: </span>**integer**

-----
[value]: #value
#### [value]
A hardware attribute's value.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[hardwareAttributeType]: #hardwareattributetype
#### [hardwareAttributeType]
The type of hardware attribute that this represents.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Attribute_Type'>SoftLayer_Hardware_Attribute_Type </a>**


## Count
</div>



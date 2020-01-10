---
title: "SoftLayer_Hardware_Component_Firmware_Attribute"
description: "The SoftLayer_Hardware_Component_Firmware_Attribute data type contains general information for a hardware model's firmwa... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Firmware_Attribute"
---

# SoftLayer_Hardware_Component_Firmware_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Firmware_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component_Firmware_Attribute data type contains general information for a hardware model's firmware. 





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
[firmwareId]: #firmwareid
#### [firmwareId]
A hardware component firmware attribute's firmware Id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A hardware component firmware attribute's Id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
A hardware component firmware attribute's type Id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[value]: #value
#### [value]
A hardware component firmware attribute's value.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[firmware]: #firmware
#### [firmware]
A hardware component firmware attribute's associated [SoftLayer_Hardware_Component_Firmware]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Firmware">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Firmware'>SoftLayer_Hardware_Component_Firmware </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
A hardware component firmware attribute's associated [SoftLayer_Hardware_Component_Firmware_Attribute_Type]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Firmware_Attribute_Type">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Firmware_Attribute_Type'>SoftLayer_Hardware_Component_Firmware_Attribute_Type </a>**


</div>

## Count
</div>



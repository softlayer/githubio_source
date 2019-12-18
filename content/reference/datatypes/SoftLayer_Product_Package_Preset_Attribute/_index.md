---
title: "SoftLayer_Product_Package_Preset_Attribute"
description: "Package preset attributes contain supplementary information for a package preset."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Preset_Attribute"
---

# SoftLayer_Product_Package_Preset_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Preset_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
Package preset attributes contain supplementary information for a package preset. 



### seeAlso

* [SoftLayer_Product_Package_Preset](/reference/services/SoftLayer_Product_Package_Preset )


* [SoftLayer_Product_Package_Preset_Attribute_Type](/reference/datatypes/SoftLayer_Product_Package_Preset_Attribute_Type )




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
[attributeTypeId]: #attributetypeid
#### [attributeTypeId]
The internal identifier of the type of attribute that a pacakge preset attribute belongs to.   
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A package preset attribute's internal identifier.   
<span class="type-label">Type: </span>**integer**

-----
[presetId]: #presetid
#### [presetId]
The internal identifier of the package preset an attribute belongs to.   
<span class="type-label">Type: </span>**integer**

-----
[value]: #value
#### [value]
A package preset's attribute value.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[attributeType]: #attributetype
#### [attributeType]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Preset_Attribute_Type'>SoftLayer_Product_Package_Preset_Attribute_Type </a>**

-----
[preset]: #preset
#### [preset]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset </a>**


## Count
</div>



---
title: "SoftLayer_Product_Item_Rule_Resource_Location"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Rule_Resource_Location"
---

# SoftLayer_Product_Item_Rule_Resource_Location
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource_Location' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
The unique identifier of the resource.  
<span class="type-label">Type: </span>**integer**

-----
[ruleId]: #ruleid
#### [ruleId]
The unique identifier of the rule this resource is included in.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[resource]: #resource
#### [resource]
A location that the associated rule applies to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[rule]: #rule
#### [rule]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Rule'>SoftLayer_Product_Item_Rule </a>**


## Count
</div>



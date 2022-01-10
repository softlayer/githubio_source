---
title: "SoftLayer_Product_Item_Rule_Resource"
description: "The item rule resource data type represents a resource that is part of an item rule. The item rule resource is used when... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Rule_Resource"
---

# SoftLayer_Product_Item_Rule_Resource
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource' >Datatype</a></li>
    </ul>
</div>

## Description 


The item rule resource data type represents a resource that is part of an item rule. The item rule resource is used when its item rule is checked on an order. 





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
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
The unique identifier of the resource.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[ruleId]: #ruleid
#### [ruleId]
The unique identifier of the rule this resource is included in.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[rule]: #rule
#### [rule]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Rule'>SoftLayer_Product_Item_Rule </a>**  



</div>

## Count
</div>



---
title: "SoftLayer_Provisioning_Maintenance_Classification"
description: "The SoftLayer_Provisioning_Maintenance_Classification represent a maintenance type for the specific hardware maintenance... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Provisioning"
classes:
    - "SoftLayer_Provisioning_Maintenance_Classification"
---

# SoftLayer_Provisioning_Maintenance_Classification
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Provisioning_Maintenance_Classification' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Provisioning_Maintenance_Classification' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Provisioning_Maintenance_Classification represent a maintenance type for the specific hardware maintenance desired. 





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
The id of the maintenance classification.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[slots]: #slots
#### [slots]
The number of slots required for the maintenance classification.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type or name of the maintenance classification.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[itemCategories]: #itemcategories
#### [itemCategories]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Maintenance_Classification_Item_Category'>SoftLayer_Provisioning_Maintenance_Classification_Item_Category[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[itemCategoryCount]: #itemcategorycount
#### [itemCategoryCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>



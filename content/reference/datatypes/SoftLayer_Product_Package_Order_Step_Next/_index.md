---
title: "SoftLayer_Product_Package_Order_Step_Next"
description: "This datatype simply describes which steps are next in line for ordering."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Order_Step_Next"
---

# SoftLayer_Product_Package_Order_Step_Next
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step_Next' >Datatype</a></li>
    </ul>
</div>

## Description 
This datatype simply describes which steps are next in line for ordering. 





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
The unique identifier for this object.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[nextOrderStepId]: #nextorderstepid
#### [nextOrderStepId]
The unique identifier for SoftLayer_Product_Package_Order_Step for the next step in the process.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[orderStepId]: #orderstepid
#### [orderStepId]
The unique identifier for SoftLayer_Product_Package_Order_Step for the current step.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[step]: #step
#### [step]
The SoftLayer_Product_Package_Order_Step to which this object belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step'>SoftLayer_Product_Package_Order_Step </a>**


</div>

## Count
</div>



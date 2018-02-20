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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique identifier for this object. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#nextOrderStepId" name=nextOrderStepId>nextOrderStepId</a></span>
            <div class='views-field-body'>The unique identifier for SoftLayer_Product_Package_Order_Step for the next step in the process. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderStepId" name=orderStepId>orderStepId</a></span>
            <div class='views-field-body'>The unique identifier for SoftLayer_Product_Package_Order_Step for the current step. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#step" name=step>step</a></span>
            <div class='views-field-body'>The SoftLayer_Product_Package_Order_Step to which this object belongs. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step'>SoftLayer_Product_Package_Order_Step </a></p></div>
        </div>
            </div>
</div>



---
title: "SoftLayer_Hardware_Component_Locator_Result"
description: "This object holds a generic component model id and the list of datacenter names where it is available."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Locator_Result"
---

# SoftLayer_Hardware_Component_Locator_Result
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Locator_Result' >Datatype</a></li>
    </ul>
</div>

## Description 
This object holds a generic component model id and the list of datacenter names where it is available. 





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
            <span class='views-field-title'>
                <a href="#datacenters" name=datacenters>datacenters</a>
            </span>
            <div class='views-field-body'>array of datacenter names where generic component model is available </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>array of strings</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#genericComponentModelId" name=genericComponentModelId>genericComponentModelId</a>
            </span>
            <div class='views-field-body'>generic component model id </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#serverPackageId" name=serverPackageId>serverPackageId</a>
            </span>
            <div class='views-field-body'>Id of SoftLayer_Product_Package_Server </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
    </div>



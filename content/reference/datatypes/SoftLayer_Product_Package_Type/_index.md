---
title: "SoftLayer_Product_Package_Type"
description: "The [[SoftLayer_Product_Package_Type]] object indicates the type for a service offering (package). The type can be used... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Type"
---

# SoftLayer_Product_Package_Type
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Type' >Datatype</a></li>
    </ul>
</div>

## Description 
The [[SoftLayer_Product_Package_Type]] object indicates the type for a service offering (package). The type can be used to filter packages. For example, if you are looking for the package representing virtual servers, you can filter on the type's key name of '''VIRTUAL_SERVER_INSTANCE'''. For bare metal servers by core or CPU, filter on '''BARE_METAL_CORE''' or '''BARE_METAL_CPU''', respectively. 





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
            <div class='views-field-body'>The package type's unique identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keyName" name=keyName>keyName</a></span>
            <div class='views-field-body'>The unique key name of the package type. Use this value when filtering. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The name of the package type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#packages" name=packages>packages</a></span>
            <div class='views-field-body'>All the packages associated with the given package type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#packageCount" name=packageCount>packageCount</a></span>
            <div class='views-field-body'>A count of all the packages associated with the given package type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>



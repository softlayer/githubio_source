---
title: "SoftLayer_Container_Virtual_Guest_Configuration_Option"
description: "An option found within a [[SoftLayer_Container_Virtual_Guest_Configuration (type)]] structure."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Virtual_Guest_Configuration_Option"
---

# SoftLayer_Container_Virtual_Guest_Configuration_Option
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Virtual_Guest_Configuration_Option' >Datatype</a></li>
    </ul>
</div>

## Description 
An option found within a [[SoftLayer_Container_Virtual_Guest_Configuration (type)]] structure. 





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
            <span class='views-field-title'><a href="#flavor" name=flavor>flavor</a></span>
            <div class='views-field-body'>
Provides a description of a pre-defined configuration with monthly and hourly costs.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemPrice" name=itemPrice>itemPrice</a></span>
            <div class='views-field-body'>
Provides hourly and monthly costs (if either are applicable), and a description of the option.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#template" name=template>template</a></span>
            <div class='views-field-body'>
Provides a fragment of the request with the properties and values that must be sent when creating a computing instance with the option.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a></p></div>
        </div>
            </div>
    </div>



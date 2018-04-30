---
title: "SoftLayer_Container_Tax_Cache_Item"
description: "This represents one order item in a tax calculation."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Tax_Cache_Item"
---

# SoftLayer_Container_Tax_Cache_Item
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Tax_Cache_Item' >Datatype</a></li>
    </ul>
</div>

## Description 
This represents one order item in a tax calculation. 





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
                <a href="#categoryCode" name=categoryCode>categoryCode</a>
            </span>
            <div class='views-field-body'>The category code for the referenced product. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#containerHash" name=containerHash>containerHash</a>
            </span>
            <div class='views-field-body'>This hash will match to the hash on an order container. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemPriceId" name=itemPriceId>itemPriceId</a>
            </span>
            <div class='views-field-body'>The reference to the price for this order item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxRates" name=taxRates>taxRates</a>
            </span>
            <div class='views-field-body'>This is the container containing the individual tax rates. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Tax_Rates'>SoftLayer_Container_Tax_Rates </a></p>
            </div>
        </div>
            </div>
    </div>



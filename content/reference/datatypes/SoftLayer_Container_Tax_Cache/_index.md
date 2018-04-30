---
title: "SoftLayer_Container_Tax_Cache"
description: "These are the results of a tax calculation. The tax calculation was kicked off but allowed to run in the background. Thi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Tax_Cache"
---

# SoftLayer_Container_Tax_Cache
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Tax_Cache' >Datatype</a></li>
    </ul>
</div>

## Description 
These are the results of a tax calculation. The tax calculation was kicked off but allowed to run in the background. This type stores the results so that an interface can be updated with up-to-date information. 





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
                <a href="#effectiveTaxRate" name=effectiveTaxRate>effectiveTaxRate</a>
            </span>
            <div class='views-field-body'>The percentage of the final total that should be tax. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#items" name=items>items</a>
            </span>
            <div class='views-field-body'>The container that holds the four actual tax rates, one for each fee type. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Tax_Cache_Item'>SoftLayer_Container_Tax_Cache_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#status" name=status>status</a>
            </span>
            <div class='views-field-body'>The status of the tax request. This should be PENDING, FAILED, or COMPLETED. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#totalTaxAmount" name=totalTaxAmount>totalTaxAmount</a>
            </span>
            <div class='views-field-body'>The final amount of tax for the order. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
            </div>
    </div>



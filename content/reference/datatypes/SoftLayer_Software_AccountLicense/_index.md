---
title: "SoftLayer_Software_AccountLicense"
description: "SoftLayer_Software_AccountLicense is a class that represents software licenses that are tied only to a customer's accoun... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_AccountLicense"
---

# SoftLayer_Software_AccountLicense
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Software_AccountLicense' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Software_AccountLicense is a class that represents software licenses that are tied only to a customer's account and not to any particular hardware, IP address, etc. 



### seeAlso

* [SoftLayer_Account](/reference/datatypes/SoftLayer_Account )


* [SoftLayer_Software_Description](/reference/datatypes/SoftLayer_Software_Description )




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
            <span class='views-field-title'><a href="#accountId" name=accountId>accountId</a></span>
            <div class='views-field-body'>The ID of the SoftLayer Account to which this Account License belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#capacity" name=capacity>capacity</a></span>
            <div class='views-field-body'>Some Account Licenses have capacity information such as CPU specified in the units key. This provides the numerical representation of the capacity of the units.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#key" name=key>key</a></span>
            <div class='views-field-body'>The License Key for this specific Account License. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#units" name=units>units</a></span>
            <div class='views-field-body'>The unit of measurement that an account license has the capacity of. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The customer account this Account License belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingItem" name=billingItem>billingItem</a></span>
            <div class='views-field-body'>The billing item for a software account license. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#softwareDescription" name=softwareDescription>softwareDescription</a></span>
            <div class='views-field-body'>The SoftLayer_Software_Description that this account license is for. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>



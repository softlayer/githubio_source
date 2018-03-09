---
title: "SoftLayer_Billing_Invoice_Item_Tax_Info"
description: "Information about the tax rates that apply to a particular invoice item."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Item_Tax_Info"
---

# SoftLayer_Billing_Invoice_Item_Tax_Info
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item_Tax_Info' >Datatype</a></li>
    </ul>
</div>

## Description 
Information about the tax rates that apply to a particular invoice item. 





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
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The date and time the tax information was recorded. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>The invoice description with special information about the invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#effectiveTaxRate" name=effectiveTaxRate>effectiveTaxRate</a>
            </span>
            <div class='views-field-body'>The tax rate that can be multiplied by the subtotal to get the </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#exemptAmount" name=exemptAmount>exemptAmount</a>
            </span>
            <div class='views-field-body'>The amount that is exempt from tax. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#feeProperty" name=feeProperty>feeProperty</a>
            </span>
            <div class='views-field-body'>The type of fee being tracked for this particular set of tax information. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>An invoice item's tax information internal identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceItemId" name=invoiceItemId>invoiceItemId</a>
            </span>
            <div class='views-field-body'>A reference to the related invoice item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceTaxInfoId" name=invoiceTaxInfoId>invoiceTaxInfoId</a>
            </span>
            <div class='views-field-body'>A reference to the tax information for the parent invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The date and time the tax information was modified. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nonTaxableBasis" name=nonTaxableBasis>nonTaxableBasis</a>
            </span>
            <div class='views-field-body'>The amount that is exempt from tax. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#reportedFlag" name=reportedFlag>reportedFlag</a>
            </span>
            <div class='views-field-body'>A flag to indicate whether this is the official record for this invoice item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sellerRegistration" name=sellerRegistration>sellerRegistration</a>
            </span>
            <div class='views-field-body'>The registration that the seller will use to report the invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxAmount" name=taxAmount>taxAmount</a>
            </span>
            <div class='views-field-body'>The tax amount associated with this line item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxAmountToCurrency" name=taxAmountToCurrency>taxAmountToCurrency</a>
            </span>
            <div class='views-field-body'>The tax amount (converted to the 'to' currency) associated with this line item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxRate" name=taxRate>taxRate</a>
            </span>
            <div class='views-field-body'>The tax rate used. Note that this might apply to only part of the </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxableBasis" name=taxableBasis>taxableBasis</a>
            </span>
            <div class='views-field-body'>The amount that is subject to tax. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#toCurrencyId" name=toCurrencyId>toCurrencyId</a>
            </span>
            <div class='views-field-body'>The currency code that the invoice is being converted to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceItem" name=invoiceItem>invoiceItem</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceTaxInfo" name=invoiceTaxInfo>invoiceTaxInfo</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Tax_Info'>SoftLayer_Billing_Invoice_Tax_Info </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#toCurrency" name=toCurrency>toCurrency</a>
            </span>
            <div class='views-field-body'>This is the currency the invoice will be converted to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Currency'>SoftLayer_Billing_Currency </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>



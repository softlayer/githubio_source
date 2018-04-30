---
title: "SoftLayer_Billing_Invoice_Tax_Info"
description: "Invoice tax information contains top-level information about the taxes recorded for a particular invoice."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Tax_Info"
---

# SoftLayer_Billing_Invoice_Tax_Info
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Invoice_Tax_Info' >Datatype</a></li>
    </ul>
</div>

## Description 
Invoice tax information contains top-level information about the taxes recorded for a particular invoice. 





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
            <div class='views-field-body'>The date and time this tax information was recorded. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#currencyId" name=currencyId>currencyId</a>
            </span>
            <div class='views-field-body'>The currency code that the invoice should be recorded in. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The internal identifier for this invoice tax information. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceId" name=invoiceId>invoiceId</a>
            </span>
            <div class='views-field-body'>A reference to the related invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The date and time this tax information was updated. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#reportedFlag" name=reportedFlag>reportedFlag</a>
            </span>
            <div class='views-field-body'>A flag to indicate whether the invoice will be auditable. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#currency" name=currency>currency</a>
            </span>
            <div class='views-field-body'>This is the currency used for the invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Currency'>SoftLayer_Billing_Currency </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#functionalCurrency" name=functionalCurrency>functionalCurrency</a>
            </span>
            <div class='views-field-body'>This is the functional currency used for the invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Currency'>SoftLayer_Billing_Currency </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoice" name=invoice>invoice</a>
            </span>
            <div class='views-field-body'>This is the related invoice for this tax-related information. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemWithCurrencyInfo" name=itemWithCurrencyInfo>itemWithCurrencyInfo</a>
            </span>
            <div class='views-field-body'>This tax information on the invoice item that includes currency details. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item_Tax_Info'>SoftLayer_Billing_Invoice_Item_Tax_Info </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#items" name=items>items</a>
            </span>
            <div class='views-field-body'>This is the collection of tax information for each of the related invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item_Tax_Info'>SoftLayer_Billing_Invoice_Item_Tax_Info[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#totalTaxAmountToCurrency" name=totalTaxAmountToCurrency>totalTaxAmountToCurrency</a>
            </span>
            <div class='views-field-body'>This the total tax amount (converted to the 'to' currency) for the invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemCount" name=itemCount>itemCount</a>
            </span>
            <div class='views-field-body'>A count of this is the collection of tax information for each of the related invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>



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

## Local
-----
[createDate]: #createdate
#### [createDate]
The date and time the tax information was recorded.  
<span class="type-label">Type: </span>**dateTime**

-----
[description]: #description
#### [description]
The invoice description with special information about the invoice.  
<span class="type-label">Type: </span>**string**

-----
[effectiveTaxRate]: #effectivetaxrate
#### [effectiveTaxRate]
The tax rate that can be multiplied by the subtotal to get the  
<span class="type-label">Type: </span>**float**

-----
[exemptAmount]: #exemptamount
#### [exemptAmount]
The amount that is exempt from tax.  
<span class="type-label">Type: </span>**float**

-----
[feeProperty]: #feeproperty
#### [feeProperty]
The type of fee being tracked for this particular set of tax information.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
An invoice item's tax information internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[invoiceItemId]: #invoiceitemid
#### [invoiceItemId]
A reference to the related invoice item.  
<span class="type-label">Type: </span>**integer**

-----
[invoiceTaxInfoId]: #invoicetaxinfoid
#### [invoiceTaxInfoId]
A reference to the tax information for the parent invoice.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date and time the tax information was modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[nonTaxableBasis]: #nontaxablebasis
#### [nonTaxableBasis]
The amount that is exempt from tax.  
<span class="type-label">Type: </span>**float**

-----
[reportedFlag]: #reportedflag
#### [reportedFlag]
A flag to indicate whether this is the official record for this invoice item.  
<span class="type-label">Type: </span>**boolean**

-----
[sellerRegistration]: #sellerregistration
#### [sellerRegistration]
The registration that the seller will use to report the invoice.  
<span class="type-label">Type: </span>**string**

-----
[taxAmount]: #taxamount
#### [taxAmount]
The tax amount associated with this line item.  
<span class="type-label">Type: </span>**float**

-----
[taxAmountToCurrency]: #taxamounttocurrency
#### [taxAmountToCurrency]
The tax amount (converted to the 'to' currency) associated with this line item.  
<span class="type-label">Type: </span>**float**

-----
[taxRate]: #taxrate
#### [taxRate]
The tax rate used. Note that this might apply to only part of the  
<span class="type-label">Type: </span>**float**

-----
[taxableBasis]: #taxablebasis
#### [taxableBasis]
The amount that is subject to tax.  
<span class="type-label">Type: </span>**float**

-----
[toCurrencyId]: #tocurrencyid
#### [toCurrencyId]
The currency code that the invoice is being converted to.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[invoiceItem]: #invoiceitem
#### [invoiceItem]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item </a>**

-----
[invoiceTaxInfo]: #invoicetaxinfo
#### [invoiceTaxInfo]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Tax_Info'>SoftLayer_Billing_Invoice_Tax_Info </a>**

-----
[toCurrency]: #tocurrency
#### [toCurrency]
This is the currency the invoice will be converted to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Currency'>SoftLayer_Billing_Currency </a>**


## Count
</div>



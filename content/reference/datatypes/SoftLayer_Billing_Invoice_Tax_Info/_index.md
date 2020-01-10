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





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date and time this tax information was recorded.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[currencyId]: #currencyid
#### [currencyId]
The currency code that the invoice should be recorded in.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The internal identifier for this invoice tax information.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[invoiceId]: #invoiceid
#### [invoiceId]
A reference to the related invoice.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date and time this tax information was updated.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[reportedFlag]: #reportedflag
#### [reportedFlag]
A flag to indicate whether the invoice will be auditable.  
<span class="type-label">Type: </span>**boolean**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[currency]: #currency
#### [currency]
This is the currency used for the invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Currency'>SoftLayer_Billing_Currency </a>**


</div>
<div class="prop-row">

-----
[functionalCurrency]: #functionalcurrency
#### [functionalCurrency]
This is the functional currency used for the invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Currency'>SoftLayer_Billing_Currency </a>**


</div>
<div class="prop-row">

-----
[invoice]: #invoice
#### [invoice]
This is the related invoice for this tax-related information.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**


</div>
<div class="prop-row">

-----
[itemWithCurrencyInfo]: #itemwithcurrencyinfo
#### [itemWithCurrencyInfo]
This tax information on the invoice item that includes currency details.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item_Tax_Info'>SoftLayer_Billing_Invoice_Item_Tax_Info </a>**


</div>
<div class="prop-row">

-----
[items]: #items
#### [items]
This is the collection of tax information for each of the related invoice items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item_Tax_Info'>SoftLayer_Billing_Invoice_Item_Tax_Info[] </a>**


</div>
<div class="prop-row">

-----
[totalTaxAmountToCurrency]: #totaltaxamounttocurrency
#### [totalTaxAmountToCurrency]
This the total tax amount (converted to the 'to' currency) for the invoice.  
<span class="type-label">Type: </span>**float**


</div>

## Count
<div class="prop-row">

-----
[itemCount]: #itemcount
#### [itemCount]
A count of this is the collection of tax information for each of the related invoice items.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>



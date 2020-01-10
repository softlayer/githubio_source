---
title: "SoftLayer_Billing_Invoice"
description: "The SoftLayer_Billing_Invoice service controls the invoices that are created whenever a SoftLayer customer's account bal... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice"
---
# SoftLayer_Billing_Invoice
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Invoice' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Invoice' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Billing_Invoice service controls the invoices that are created whenever a SoftLayer customer's account balance changes. Invoices exist in the following states: 
*'''OPEN''': Invoices which have not been paid yet. Invoices are created in the OPEN state.
*'''CLOSED''': Invoices that SoftLayer has received payment for.
*'''CLOSED_FAILED''': Invoices which were closed but were not paid for. Customers who are terminated for non-payment typically have invoices in this state.


Once an invoice is paid it moves from OPEN to CLOSED state. Invoices are created under varying types, which are defined in the type property of the [SoftLayer_Invoice]({{<ref "reference/datatypes/SoftLayer_Invoice">}}). Invoices are created under one of the following type categories: 
*'''NEW''': An invoice for new service. A SoftLayer customer's first invoice is of the NEW type.
*'''RECURRING''': Invoices that are generated on a SoftLayer customer's anniversary billing date for monthly services.
*'''ONE-TIME-CHARGE''': Invoices that are generated when one-time charges are applied to an account for fees incurred from products or services procured outside of the standard purchasing processes.
*'''CREDIT''': Invoices that are generated whenever SoftLayer applies a credit against an account's balance.
*'''REFUND''': Account credits that are applied against a customer's account balance along with the receivables on their account. REFUND type invoices are generated whenever a customer receives a service credit on their account balance and has their invoice items changed due to the credit.
*'''MANUAL_PAYMENT_CREDIT''': Invoice credits that are generated whenever a customer makes a manual payment.


Invoices are created with contact information duplicated from the [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}). We do this in order to maintain a history of an account's contact information as invoices are generated. Likewise each invoice record keeps track of an account's balance as the invoice is opened and closed. 

Query the [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) service to get a list of invoices for your account. 


### associatedMethods

*  [SoftLayer_Account::getBalance](/reference/services/SoftLayer_Account/getBalance )
*  [SoftLayer_Account::getInvoices](/reference/services/SoftLayer_Account/getInvoices )



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [emailInvoices](/reference/services/SoftLayer_Billing_Invoice/emailInvoices)
Create a transaction to email invoice links.
</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Billing_Invoice/getAccount)
Retrieve the account that an invoice belongs to.
</div>

<div class="method-row">

#### [getAmount](/reference/services/SoftLayer_Billing_Invoice/getAmount)
Retrieve this is the amount of this invoice.
</div>

<div class="method-row">

#### [getBrandAtInvoiceCreation](/reference/services/SoftLayer_Billing_Invoice/getBrandAtInvoiceCreation)

</div>

<div class="method-row">

#### [getDetailedPdfGeneratedFlag](/reference/services/SoftLayer_Billing_Invoice/getDetailedPdfGeneratedFlag)
Retrieve a flag that will reflect whether the detailed version of the pdf has been generated.
</div>

<div class="method-row">

#### [getExcel](/reference/services/SoftLayer_Billing_Invoice/getExcel)
Retrieve a Microsoft Excel copy of an invoice.
</div>

<div class="method-row">

#### [getInvoiceTopLevelItems](/reference/services/SoftLayer_Billing_Invoice/getInvoiceTopLevelItems)
Retrieve a list of top-level invoice items that are on the currently pending invoice.
</div>

<div class="method-row">

#### [getInvoiceTotalAmount](/reference/services/SoftLayer_Billing_Invoice/getInvoiceTotalAmount)
Retrieve the total amount of this invoice.
</div>

<div class="method-row">

#### [getInvoiceTotalOneTimeAmount](/reference/services/SoftLayer_Billing_Invoice/getInvoiceTotalOneTimeAmount)
Retrieve the total one-time charges for this invoice. This is the sum of one-time charges + setup fees + labor fees. This does not include taxes.
</div>

<div class="method-row">

#### [getInvoiceTotalOneTimeTaxAmount](/reference/services/SoftLayer_Billing_Invoice/getInvoiceTotalOneTimeTaxAmount)
Retrieve a sum of all the taxes related to one time charges for this invoice.
</div>

<div class="method-row">

#### [getInvoiceTotalPreTaxAmount](/reference/services/SoftLayer_Billing_Invoice/getInvoiceTotalPreTaxAmount)
Retrieve the total amount of this invoice. This does not include taxes.
</div>

<div class="method-row">

#### [getInvoiceTotalRecurringAmount](/reference/services/SoftLayer_Billing_Invoice/getInvoiceTotalRecurringAmount)
Retrieve the total Recurring amount of this invoice. This amount does not include taxes or one time charges.
</div>

<div class="method-row">

#### [getInvoiceTotalRecurringTaxAmount](/reference/services/SoftLayer_Billing_Invoice/getInvoiceTotalRecurringTaxAmount)
Retrieve the total amount of the recurring taxes on this invoice.
</div>

<div class="method-row">

#### [getItems](/reference/services/SoftLayer_Billing_Invoice/getItems)
Retrieve the items that belong to this invoice.
</div>

<div class="method-row">

#### [getLocalCurrencyExchangeRate](/reference/services/SoftLayer_Billing_Invoice/getLocalCurrencyExchangeRate)
Retrieve exchange rate used for billing this invoice.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Billing_Invoice/getObject)
Retrieve a SoftLayer_Billing_Invoice record.
</div>

<div class="method-row">

#### [getPayment](/reference/services/SoftLayer_Billing_Invoice/getPayment)
Retrieve this is the total payment made on this invoice.
</div>

<div class="method-row">

#### [getPayments](/reference/services/SoftLayer_Billing_Invoice/getPayments)
Retrieve the payments for the invoice.
</div>

<div class="method-row">

#### [getPdf](/reference/services/SoftLayer_Billing_Invoice/getPdf)
Retrieve a PDF copy of an invoice.
</div>

<div class="method-row">

#### [getPdfDetailed](/reference/services/SoftLayer_Billing_Invoice/getPdfDetailed)
Retrieve a PDF copy of the detailed invoice summary.
</div>

<div class="method-row">

#### [getPdfDetailedFilename](/reference/services/SoftLayer_Billing_Invoice/getPdfDetailedFilename)
Get the name of the detailed version of the PDF.
</div>

<div class="method-row">

#### [getPdfFileSize](/reference/services/SoftLayer_Billing_Invoice/getPdfFileSize)
Retrieve the size of a PDF copy of an invoice.
</div>

<div class="method-row">

#### [getPdfFilename](/reference/services/SoftLayer_Billing_Invoice/getPdfFilename)

</div>

<div class="method-row">

#### [getPreliminaryExcel](/reference/services/SoftLayer_Billing_Invoice/getPreliminaryExcel)
Retrieve a Microsoft Excel copy of an invoice.
</div>

<div class="method-row">

#### [getPreliminaryPdf](/reference/services/SoftLayer_Billing_Invoice/getPreliminaryPdf)
Retrieve a PDF copy of an invoice.
</div>

<div class="method-row">

#### [getPreliminaryPdfDetailed](/reference/services/SoftLayer_Billing_Invoice/getPreliminaryPdfDetailed)
Retrieve a PDF copy of the detailed version of an invoice.
</div>

<div class="method-row">

#### [getSellerRegistration](/reference/services/SoftLayer_Billing_Invoice/getSellerRegistration)
Retrieve this is the seller's tax registration.
</div>

<div class="method-row">

#### [getTaxInfo](/reference/services/SoftLayer_Billing_Invoice/getTaxInfo)
Retrieve this is the tax information that applies to tax auditing. This is the official tax record for this invoice.
</div>

<div class="method-row">

#### [getTaxInfoHistory](/reference/services/SoftLayer_Billing_Invoice/getTaxInfoHistory)
Retrieve this is the set of tax information for any tax calculation for this invoice. Note that not all of these are necessarily official, so use the taxInfo key to get the final information.
</div>

<div class="method-row">

#### [getTaxMessage](/reference/services/SoftLayer_Billing_Invoice/getTaxMessage)
Retrieve this is a message explaining the tax treatment for this invoice.
</div>

<div class="method-row">

#### [getTaxType](/reference/services/SoftLayer_Billing_Invoice/getTaxType)
Retrieve this is the strategy used to calculate tax on this invoice.
</div>

<div class="method-row">

#### [getXlsFilename](/reference/services/SoftLayer_Billing_Invoice/getXlsFilename)

</div>

<div class="method-row">

#### [getZeroFeeItemCounts](/reference/services/SoftLayer_Billing_Invoice/getZeroFeeItemCounts)

</div>
</div>

</div>


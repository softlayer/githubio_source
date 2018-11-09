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


Once an invoice is paid it moves from OPEN to CLOSED state. Invoices are created under varying types, which are defined in the type property of the [[SoftLayer_Invoice (type)|SoftLayer_Invoice data type]]. Invoices are created under one of the following type categories: 
*'''NEW''': An invoice for new service. A SoftLayer customer's first invoice is of the NEW type.
*'''RECURRING''': Invoices that are generated on a SoftLayer customer's anniversary billing date for monthly services.
*'''ONE-TIME-CHARGE''': Invoices that are generated when one-time charges are applied to an account for fees incurred from products or services procured outside of the standard purchasing processes.
*'''CREDIT''': Invoices that are generated whenever SoftLayer applies a credit against an account's balance.
*'''REFUND''': Account credits that are applied against a customer's account balance along with the receivables on their account. REFUND type invoices are generated whenever a customer receives a service credit on their account balance and has their invoice items changed due to the credit.
*'''MANUAL_PAYMENT_CREDIT''': Invoice credits that are generated whenever a customer makes a manual payment.


Invoices are created with contact information duplicated from the [[SoftLayer_Account (type)|SoftLayer_Account data type]]. We do this in order to maintain a history of an account's contact information as invoices are generated. Likewise each invoice record keeps track of an account's balance as the invoice is opened and closed. 

Query the [[SoftLayer_Account]] service to get a list of invoices for your account. 


### associatedMethods

*  [SoftLayer_Account::getBalance](/reference/services/SoftLayer_Account/getBalance )
*  [SoftLayer_Account::getInvoices](/reference/services/SoftLayer_Account/getInvoices )



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/emailInvoices'> emailInvoices</a> </span>
            <div class='views-field-body'>Create a transaction to email invoice links.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account that an invoice belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getAmount'> getAmount</a> </span>
            <div class='views-field-body'>Retrieve this is the amount of this invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getBrandAtInvoiceCreation'> getBrandAtInvoiceCreation</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getDetailedPdfGeneratedFlag'> getDetailedPdfGeneratedFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag that will reflect whether the detailed version of the pdf has been generated.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getExcel'> getExcel</a> </span>
            <div class='views-field-body'>Retrieve a Microsoft Excel copy of an invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getInvoiceTopLevelItems'> getInvoiceTopLevelItems</a> </span>
            <div class='views-field-body'>Retrieve a list of top-level invoice items that are on the currently pending invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getInvoiceTotalAmount'> getInvoiceTotalAmount</a> </span>
            <div class='views-field-body'>Retrieve the total amount of this invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getInvoiceTotalOneTimeAmount'> getInvoiceTotalOneTimeAmount</a> </span>
            <div class='views-field-body'>Retrieve the total one-time charges for this invoice. This is the sum of one-time charges + setup fees + labor fees. This does not include taxes.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getInvoiceTotalOneTimeTaxAmount'> getInvoiceTotalOneTimeTaxAmount</a> </span>
            <div class='views-field-body'>Retrieve a sum of all the taxes related to one time charges for this invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getInvoiceTotalPreTaxAmount'> getInvoiceTotalPreTaxAmount</a> </span>
            <div class='views-field-body'>Retrieve the total amount of this invoice. This does not include taxes.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getInvoiceTotalRecurringAmount'> getInvoiceTotalRecurringAmount</a> </span>
            <div class='views-field-body'>Retrieve the total Recurring amount of this invoice. This amount does not include taxes or one time charges.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getInvoiceTotalRecurringTaxAmount'> getInvoiceTotalRecurringTaxAmount</a> </span>
            <div class='views-field-body'>Retrieve the total amount of the recurring taxes on this invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getItems'> getItems</a> </span>
            <div class='views-field-body'>Retrieve the items that belong to this invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getLocalCurrencyExchangeRate'> getLocalCurrencyExchangeRate</a> </span>
            <div class='views-field-body'>Retrieve exchange rate used for billing this invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Billing_Invoice record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getPayment'> getPayment</a> </span>
            <div class='views-field-body'>Retrieve this is the total payment made on this invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getPayments'> getPayments</a> </span>
            <div class='views-field-body'>Retrieve the payments for the invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getPdf'> getPdf</a> </span>
            <div class='views-field-body'>Retrieve a PDF copy of an invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getPdfDetailed'> getPdfDetailed</a> </span>
            <div class='views-field-body'>Retrieve a PDF copy of the detailed invoice summary.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getPdfDetailedFilename'> getPdfDetailedFilename</a> </span>
            <div class='views-field-body'>Get the name of the detailed version of the PDF.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getPdfFileSize'> getPdfFileSize</a> </span>
            <div class='views-field-body'>Retrieve the size of a PDF copy of an invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getPdfFilename'> getPdfFilename</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getPreliminaryExcel'> getPreliminaryExcel</a> </span>
            <div class='views-field-body'>Retrieve a Microsoft Excel copy of an invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getPreliminaryPdf'> getPreliminaryPdf</a> </span>
            <div class='views-field-body'>Retrieve a PDF copy of an invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getPreliminaryPdfDetailed'> getPreliminaryPdfDetailed</a> </span>
            <div class='views-field-body'>Retrieve a PDF copy of the detailed version of an invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getSellerRegistration'> getSellerRegistration</a> </span>
            <div class='views-field-body'>Retrieve this is the seller's tax registration.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getTaxInfo'> getTaxInfo</a> </span>
            <div class='views-field-body'>Retrieve this is the tax information that applies to tax auditing. This is the official tax record for this invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getTaxInfoHistory'> getTaxInfoHistory</a> </span>
            <div class='views-field-body'>Retrieve this is the set of tax information for any tax calculation for this invoice. Note that not all of these are necessarily official, so use the taxInfo key to get the final information.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getTaxMessage'> getTaxMessage</a> </span>
            <div class='views-field-body'>Retrieve this is a message explaining the tax treatment for this invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getTaxType'> getTaxType</a> </span>
            <div class='views-field-body'>Retrieve this is the strategy used to calculate tax on this invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getXlsFilename'> getXlsFilename</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice/getZeroFeeItemCounts'> getZeroFeeItemCounts</a> </span>
            <div class='views-field-body'></div>
        </div>
        </div>
</div>


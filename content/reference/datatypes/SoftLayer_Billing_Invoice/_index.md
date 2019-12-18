---
title: "SoftLayer_Billing_Invoice"
description: "The SoftLayer_Billing_Invoice data type contains general information relating to an individual invoice applied to a Soft... "
layout: "datatype"
tags:
    - "datatype"
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
The SoftLayer_Billing_Invoice data type contains general information relating to an individual invoice applied to a SoftLayer customer account. Personal information in this type such as names, addresses, and phone numbers are taken from the account's contact information at the time the invoice is generated. 


### associatedMethods

*  [SoftLayer_Billing_Invoice::getObject](/reference/services/SoftLayer_Billing_Invoice/getObject )
*  [SoftLayer_Account::getInvoices](/reference/services/SoftLayer_Account/getInvoices )



### seeAlso

* [SoftLayer_Account (type)](/reference/datatypes/SoftLayer_Account (type) )




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
[accountId]: #accountid
#### [accountId]
The SoftLayer customer account that an invoice belongs to.  
<span class="type-label">Type: </span>**integer**

-----
[address1]: #address1
#### [address1]
The first line of an address belonging to an account at the time an invoice is created.  
<span class="type-label">Type: </span>**string**

-----
[address2]: #address2
#### [address2]
The second line of an address belonging to an account at the time an invoice is created.  
<span class="type-label">Type: </span>**string**

-----
[city]: #city
#### [city]
The city portion of an address belonging to an account at the time an invoice is created.  
<span class="type-label">Type: </span>**string**

-----
[claimedTaxExemptTxFlag]: #claimedtaxexempttxflag
#### [claimedTaxExemptTxFlag]
Whether an account was exempt from taxes on their invoices at the time an invoice is created.  
<span class="type-label">Type: </span>**boolean**

-----
[closedDate]: #closeddate
#### [closedDate]
The date an invoice was closed. Open invoices have a null closed date.  
<span class="type-label">Type: </span>**dateTime**

-----
[companyName]: #companyname
#### [companyName]
The company name belonging to an account at the time an invoice is created.  
<span class="type-label">Type: </span>**string**

-----
[country]: #country
#### [country]
A two-letter abbreviation of the country portion of an address belonging to an account at the time an invoice is created.  
<span class="type-label">Type: </span>**string**

-----
[createDate]: #createdate
#### [createDate]
The date an invoice was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[documentsGeneratedFlag]: #documentsgeneratedflag
#### [documentsGeneratedFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[email]: #email
#### [email]
The email address belonging to an account at the time an invoice is created.  
<span class="type-label">Type: </span>**string**

-----
[endingBalance]: #endingbalance
#### [endingBalance]
An SoftLayer account's balance at the time an invoice is closed. This value is measured in US Dollar ($USD) currency.  
<span class="type-label">Type: </span>**decimal**

-----
[faxPhone]: #faxphone
#### [faxPhone]
The fax telephone number belonging to an account at the time an invoice is created.  
<span class="type-label">Type: </span>**string**

-----
[firstName]: #firstname
#### [firstName]
The first name of the account holder at the time an invoice is created.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
An invoice's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[lastName]: #lastname
#### [lastName]
The last name of the account holder at the time an invoice is created.  
<span class="type-label">Type: </span>**string**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date an invoice was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[officePhone]: #officephone
#### [officePhone]
The telephone number belonging to an account at the time an invoice is created.  
<span class="type-label">Type: </span>**string**

-----
[postalCode]: #postalcode
#### [postalCode]
The postal code portion of an address belonging to an account at the time an invoice is created.  
<span class="type-label">Type: </span>**string**

-----
[purchaseOrderNumber]: #purchaseordernumber
#### [purchaseOrderNumber]
  
<span class="type-label">Type: </span>**string**

-----
[startingBalance]: #startingbalance
#### [startingBalance]
An SoftLayer account's balance at the time an invoice is created. This value is measured in US Dollar ($USD) currency.  
<span class="type-label">Type: </span>**decimal**

-----
[state]: #state
#### [state]
A two-letter abbreviation of the state portion of an address belonging to an account at the time an invoice is created. If the account that the invoice was generated for resides outside a province then this is set to "other".  
<span class="type-label">Type: </span>**string**

-----
[statusCode]: #statuscode
#### [statusCode]
An invoice's status. The "OPEN" status means SoftLayer has not yet received payment for this invoice. "CLOSED" status means that SoftLayer has received payment and closed the invoice. The "CLOSED_FAILED" status code means SoftLayer closed the invoice without receiving a payment. Invoices are usually set to CLOSED_FAILED status in cases where customer accounts are terminated for non-payment.   
<span class="type-label">Type: </span>**string**

-----
[taxStatusId]: #taxstatusid
#### [taxStatusId]
  
<span class="type-label">Type: </span>**integer**

-----
[taxTypeId]: #taxtypeid
#### [taxTypeId]
  
<span class="type-label">Type: </span>**integer**

-----
[typeCode]: #typecode
#### [typeCode]
An invoice's type. SoftLayer invoices and service credits are differentiated by their type. The "NEW" type code signifies an invoice for new service. A SoftLayer customer's first invoice has the NEW type code. "RECURRING" invoices are generated on a SoftLayer customer's anniversary billing date for monthly services. "ONE-TIME-CHARGE" invoices are generated when one-time charges are applied to an account. "CREDIT" invoices are generated whenever SoftLayer applies a credit against an account's balance. There are two special types of service credits. "REFUND" type credits are applied against a customer's account balance along with the receivables on their account. "MANUAL_PAYMENT_CREDIT" invoice credits are generated whenever a customer makes an unscheduled payment.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account that an invoice belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[amount]: #amount
#### [amount]
This is the amount of this invoice.  
<span class="type-label">Type: </span>**decimal**

-----
[brandAtInvoiceCreation]: #brandatinvoicecreation
#### [brandAtInvoiceCreation]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a>**

-----
[detailedPdfGeneratedFlag]: #detailedpdfgeneratedflag
#### [detailedPdfGeneratedFlag]
A flag that will reflect whether the detailed version of the pdf has been generated.  
<span class="type-label">Type: </span>**boolean**

-----
[invoiceTopLevelItems]: #invoicetoplevelitems
#### [invoiceTopLevelItems]
A list of top-level invoice items that are on the currently pending invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>**

-----
[invoiceTotalAmount]: #invoicetotalamount
#### [invoiceTotalAmount]
The total amount of this invoice.  
<span class="type-label">Type: </span>**decimal**

-----
[invoiceTotalOneTimeAmount]: #invoicetotalonetimeamount
#### [invoiceTotalOneTimeAmount]
The total one-time charges for this invoice. This is the sum of one-time charges + setup fees + labor fees. This does not include taxes.  
<span class="type-label">Type: </span>**decimal**

-----
[invoiceTotalOneTimeTaxAmount]: #invoicetotalonetimetaxamount
#### [invoiceTotalOneTimeTaxAmount]
A sum of all the taxes related to one time charges for this invoice.  
<span class="type-label">Type: </span>**decimal**

-----
[invoiceTotalPreTaxAmount]: #invoicetotalpretaxamount
#### [invoiceTotalPreTaxAmount]
The total amount of this invoice. This does not include taxes.  
<span class="type-label">Type: </span>**decimal**

-----
[invoiceTotalRecurringAmount]: #invoicetotalrecurringamount
#### [invoiceTotalRecurringAmount]
The total Recurring amount of this invoice. This amount does not include taxes or one time charges.  
<span class="type-label">Type: </span>**decimal**

-----
[invoiceTotalRecurringTaxAmount]: #invoicetotalrecurringtaxamount
#### [invoiceTotalRecurringTaxAmount]
The total amount of the recurring taxes on this invoice.  
<span class="type-label">Type: </span>**decimal**

-----
[items]: #items
#### [items]
The items that belong to this invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>**

-----
[localCurrencyExchangeRate]: #localcurrencyexchangerate
#### [localCurrencyExchangeRate]
Exchange rate used for billing this invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Currency_ExchangeRate'>SoftLayer_Billing_Currency_ExchangeRate </a>**

-----
[payment]: #payment
#### [payment]
This is the total payment made on this invoice.  
<span class="type-label">Type: </span>**decimal**

-----
[payments]: #payments
#### [payments]
The payments for the invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Receivable_Payment'>SoftLayer_Billing_Invoice_Receivable_Payment[] </a>**

-----
[sellerRegistration]: #sellerregistration
#### [sellerRegistration]
This is the seller's tax registration.  
<span class="type-label">Type: </span>**string**

-----
[taxInfo]: #taxinfo
#### [taxInfo]
This is the tax information that applies to tax auditing. This is the official tax record for this invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Tax_Info'>SoftLayer_Billing_Invoice_Tax_Info </a>**

-----
[taxInfoHistory]: #taxinfohistory
#### [taxInfoHistory]
This is the set of tax information for any tax calculation for this invoice. Note that not all of these are necessarily official, so use the taxInfo key to get the final information.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Tax_Info'>SoftLayer_Billing_Invoice_Tax_Info[] </a>**

-----
[taxMessage]: #taxmessage
#### [taxMessage]
This is a message explaining the tax treatment for this invoice.  
<span class="type-label">Type: </span>**string**

-----
[taxType]: #taxtype
#### [taxType]
This is the strategy used to calculate tax on this invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Tax_Type'>SoftLayer_Billing_Invoice_Tax_Type </a>**


## Count

-----
[invoiceTopLevelItemCount]: #invoicetoplevelitemcount
#### [invoiceTopLevelItemCount]
A count of a list of top-level invoice items that are on the currently pending invoice.   
<span class="type-label">Type: </span>**unsigned long**


-----
[itemCount]: #itemcount
#### [itemCount]
A count of the items that belong to this invoice.   
<span class="type-label">Type: </span>**unsigned long**


-----
[paymentCount]: #paymentcount
#### [paymentCount]
A count of the payments for the invoice.   
<span class="type-label">Type: </span>**unsigned long**


-----
[taxInfoHistoryCount]: #taxinfohistorycount
#### [taxInfoHistoryCount]
A count of this is the set of tax information for any tax calculation for this invoice. Note that not all of these are necessarily official, so use the taxInfo key to get the final information.   
<span class="type-label">Type: </span>**unsigned long**

</div>



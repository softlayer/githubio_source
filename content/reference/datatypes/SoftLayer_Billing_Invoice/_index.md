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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountId" name=accountId>accountId</a>
            </span>
            <div class='views-field-body'>The SoftLayer customer account that an invoice belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#address1" name=address1>address1</a>
            </span>
            <div class='views-field-body'>The first line of an address belonging to an account at the time an invoice is created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#address2" name=address2>address2</a>
            </span>
            <div class='views-field-body'>The second line of an address belonging to an account at the time an invoice is created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#city" name=city>city</a>
            </span>
            <div class='views-field-body'>The city portion of an address belonging to an account at the time an invoice is created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#claimedTaxExemptTxFlag" name=claimedTaxExemptTxFlag>claimedTaxExemptTxFlag</a>
            </span>
            <div class='views-field-body'>Whether an account was exempt from taxes on their invoices at the time an invoice is created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#closedDate" name=closedDate>closedDate</a>
            </span>
            <div class='views-field-body'>The date an invoice was closed. Open invoices have a null closed date. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#companyName" name=companyName>companyName</a>
            </span>
            <div class='views-field-body'>The company name belonging to an account at the time an invoice is created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#country" name=country>country</a>
            </span>
            <div class='views-field-body'>A two-letter abbreviation of the country portion of an address belonging to an account at the time an invoice is created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The date an invoice was created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#documentsGeneratedFlag" name=documentsGeneratedFlag>documentsGeneratedFlag</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#email" name=email>email</a>
            </span>
            <div class='views-field-body'>The email address belonging to an account at the time an invoice is created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#endingBalance" name=endingBalance>endingBalance</a>
            </span>
            <div class='views-field-body'>An SoftLayer account's balance at the time an invoice is closed. This value is measured in US Dollar ($USD) currency. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#faxPhone" name=faxPhone>faxPhone</a>
            </span>
            <div class='views-field-body'>The fax telephone number belonging to an account at the time an invoice is created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#firstName" name=firstName>firstName</a>
            </span>
            <div class='views-field-body'>The first name of the account holder at the time an invoice is created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>An invoice's internal identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#lastName" name=lastName>lastName</a>
            </span>
            <div class='views-field-body'>The last name of the account holder at the time an invoice is created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The date an invoice was last modified. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#officePhone" name=officePhone>officePhone</a>
            </span>
            <div class='views-field-body'>The telephone number belonging to an account at the time an invoice is created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#postalCode" name=postalCode>postalCode</a>
            </span>
            <div class='views-field-body'>The postal code portion of an address belonging to an account at the time an invoice is created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#purchaseOrderNumber" name=purchaseOrderNumber>purchaseOrderNumber</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#startingBalance" name=startingBalance>startingBalance</a>
            </span>
            <div class='views-field-body'>An SoftLayer account's balance at the time an invoice is created. This value is measured in US Dollar ($USD) currency. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#state" name=state>state</a>
            </span>
            <div class='views-field-body'>A two-letter abbreviation of the state portion of an address belonging to an account at the time an invoice is created. If the account that the invoice was generated for resides outside a province then this is set to "other". </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#statusCode" name=statusCode>statusCode</a>
            </span>
            <div class='views-field-body'>An invoice's status. The "OPEN" status means SoftLayer has not yet received payment for this invoice. "CLOSED" status means that SoftLayer has received payment and closed the invoice. The "CLOSED_FAILED" status code means SoftLayer closed the invoice without receiving a payment. Invoices are usually set to CLOSED_FAILED status in cases where customer accounts are terminated for non-payment.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxStatusId" name=taxStatusId>taxStatusId</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxTypeId" name=taxTypeId>taxTypeId</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#typeCode" name=typeCode>typeCode</a>
            </span>
            <div class='views-field-body'>An invoice's type. SoftLayer invoices and service credits are differentiated by their type. The "NEW" type code signifies an invoice for new service. A SoftLayer customer's first invoice has the NEW type code. "RECURRING" invoices are generated on a SoftLayer customer's anniversary billing date for monthly services. "ONE-TIME-CHARGE" invoices are generated when one-time charges are applied to an account. "CREDIT" invoices are generated whenever SoftLayer applies a credit against an account's balance. There are two special types of service credits. "REFUND" type credits are applied against a customer's account balance along with the receivables on their account. "MANUAL_PAYMENT_CREDIT" invoice credits are generated whenever a customer makes an unscheduled payment.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The account that an invoice belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#amount" name=amount>amount</a>
            </span>
            <div class='views-field-body'>This is the amount of this invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#brandAtInvoiceCreation" name=brandAtInvoiceCreation>brandAtInvoiceCreation</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#detailedPdfGeneratedFlag" name=detailedPdfGeneratedFlag>detailedPdfGeneratedFlag</a>
            </span>
            <div class='views-field-body'>A flag that will reflect whether the detailed version of the pdf has been generated. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceTopLevelItems" name=invoiceTopLevelItems>invoiceTopLevelItems</a>
            </span>
            <div class='views-field-body'>A list of top-level invoice items that are on the currently pending invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceTotalAmount" name=invoiceTotalAmount>invoiceTotalAmount</a>
            </span>
            <div class='views-field-body'>The total amount of this invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceTotalOneTimeAmount" name=invoiceTotalOneTimeAmount>invoiceTotalOneTimeAmount</a>
            </span>
            <div class='views-field-body'>The total one-time charges for this invoice. This is the sum of one-time charges + setup fees + labor fees. This does not include taxes. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceTotalOneTimeTaxAmount" name=invoiceTotalOneTimeTaxAmount>invoiceTotalOneTimeTaxAmount</a>
            </span>
            <div class='views-field-body'>A sum of all the taxes related to one time charges for this invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceTotalPreTaxAmount" name=invoiceTotalPreTaxAmount>invoiceTotalPreTaxAmount</a>
            </span>
            <div class='views-field-body'>The total amount of this invoice. This does not include taxes. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceTotalRecurringAmount" name=invoiceTotalRecurringAmount>invoiceTotalRecurringAmount</a>
            </span>
            <div class='views-field-body'>The total Recurring amount of this invoice. This amount does not include taxes or one time charges. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceTotalRecurringTaxAmount" name=invoiceTotalRecurringTaxAmount>invoiceTotalRecurringTaxAmount</a>
            </span>
            <div class='views-field-body'>The total amount of the recurring taxes on this invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#items" name=items>items</a>
            </span>
            <div class='views-field-body'>The items that belong to this invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#localCurrencyExchangeRate" name=localCurrencyExchangeRate>localCurrencyExchangeRate</a>
            </span>
            <div class='views-field-body'>Exchange rate used for billing this invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Currency_ExchangeRate'>SoftLayer_Billing_Currency_ExchangeRate </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#payment" name=payment>payment</a>
            </span>
            <div class='views-field-body'>This is the total payment made on this invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#payments" name=payments>payments</a>
            </span>
            <div class='views-field-body'>The payments for the invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Receivable_Payment'>SoftLayer_Billing_Invoice_Receivable_Payment[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sellerRegistration" name=sellerRegistration>sellerRegistration</a>
            </span>
            <div class='views-field-body'>This is the seller's tax registration. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxInfo" name=taxInfo>taxInfo</a>
            </span>
            <div class='views-field-body'>This is the tax information that applies to tax auditing. This is the official tax record for this invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Tax_Info'>SoftLayer_Billing_Invoice_Tax_Info </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxInfoHistory" name=taxInfoHistory>taxInfoHistory</a>
            </span>
            <div class='views-field-body'>This is the set of tax information for any tax calculation for this invoice. Note that not all of these are necessarily official, so use the taxInfo key to get the final information. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Tax_Info'>SoftLayer_Billing_Invoice_Tax_Info[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxMessage" name=taxMessage>taxMessage</a>
            </span>
            <div class='views-field-body'>This is a message explaining the tax treatment for this invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxType" name=taxType>taxType</a>
            </span>
            <div class='views-field-body'>This is the strategy used to calculate tax on this invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Tax_Type'>SoftLayer_Billing_Invoice_Tax_Type </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceTopLevelItemCount" name=invoiceTopLevelItemCount>invoiceTopLevelItemCount</a>
            </span>
            <div class='views-field-body'>A count of a list of top-level invoice items that are on the currently pending invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemCount" name=itemCount>itemCount</a>
            </span>
            <div class='views-field-body'>A count of the items that belong to this invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#paymentCount" name=paymentCount>paymentCount</a>
            </span>
            <div class='views-field-body'>A count of the payments for the invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxInfoHistoryCount" name=taxInfoHistoryCount>taxInfoHistoryCount</a>
            </span>
            <div class='views-field-body'>A count of this is the set of tax information for any tax calculation for this invoice. Note that not all of these are necessarily official, so use the taxInfo key to get the final information. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>



---
title: "SoftLayer_Billing_Invoice_Receivable_Payment"
description: "The SoftLayer_Billing_Invoice_Receivable_Payment data type contains general information relating to payments made agains... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Receivable_Payment"
---

# SoftLayer_Billing_Invoice_Receivable_Payment
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Invoice_Receivable_Payment' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Billing_Invoice_Receivable_Payment data type contains general information relating to payments made against invoices. 





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
[amount]: #amount
#### [amount]
The amount of the payment.  
<span class="type-label">Type: </span>**decimal**

-----
[createDate]: #createdate
#### [createDate]
The date of the payment.  
<span class="type-label">Type: </span>**dateTime**

-----
[invoiceId]: #invoiceid
#### [invoiceId]
The invoice that the payment is for.  
<span class="type-label">Type: </span>**integer**

-----
[typeCode]: #typecode
#### [typeCode]
The type of payment.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[creditCardLastFourDigits]: #creditcardlastfourdigits
#### [creditCardLastFourDigits]
  
<span class="type-label">Type: </span>**integer**

-----
[creditCardRequestId]: #creditcardrequestid
#### [creditCardRequestId]
  
<span class="type-label">Type: </span>**string**

-----
[creditCardTransaction]: #creditcardtransaction
#### [creditCardTransaction]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_Transaction'>SoftLayer_Billing_Payment_Card_Transaction </a>**

-----
[exchangeRate]: #exchangerate
#### [exchangeRate]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Currency_ExchangeRate'>SoftLayer_Billing_Currency_ExchangeRate </a>**

-----
[invoice]: #invoice
#### [invoice]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**

-----
[paypalTransaction]: #paypaltransaction
#### [paypalTransaction]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_PayPal_Transaction'>SoftLayer_Billing_Payment_PayPal_Transaction </a>**


## Count
</div>



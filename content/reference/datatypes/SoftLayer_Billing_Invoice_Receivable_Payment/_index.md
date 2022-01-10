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
[amount]: #amount
#### [amount]
The amount of the payment.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date of the payment.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[invoiceId]: #invoiceid
#### [invoiceId]
The invoice that the payment is for.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[typeCode]: #typecode
#### [typeCode]
The type of payment.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[creditCardTransaction]: #creditcardtransaction
#### [creditCardTransaction]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_Transaction'>SoftLayer_Billing_Payment_Card_Transaction </a>**  



</div>
<div class="prop-row">

-----
[exchangeRate]: #exchangerate
#### [exchangeRate]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Currency_ExchangeRate'>SoftLayer_Billing_Currency_ExchangeRate </a>**  



</div>
<div class="prop-row">

-----
[invoice]: #invoice
#### [invoice]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**  



</div>
<div class="prop-row">

-----
[paypalTransaction]: #paypaltransaction
#### [paypalTransaction]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_PayPal_Transaction'>SoftLayer_Billing_Payment_PayPal_Transaction </a>**  



</div>

## Count
</div>



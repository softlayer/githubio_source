---
title: "SoftLayer_Billing_Payment_PayPal_Transaction"
description: "The SoftLayer_Billing_Payment_PayPal_Transaction data type contains general information relating to attempted PayPal tra... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Payment_PayPal_Transaction"
---

# SoftLayer_Billing_Payment_PayPal_Transaction
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Payment_PayPal_Transaction' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Billing_Payment_PayPal_Transaction data type contains general information relating to attempted PayPal transactions. 





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
[accountId]: #accountid
#### [accountId]
The account ID to which the PayPal and billing information is associated with.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[addressCityName]: #addresscityname
#### [addressCityName]
City given in the address of the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[addressCountry]: #addresscountry
#### [addressCountry]
Country given in the named address of the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[addressName]: #addressname
#### [addressName]
Name given to the address provided for the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[addressPostalCode]: #addresspostalcode
#### [addressPostalCode]
Postal Code of the address of the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[addressStateProvence]: #addressstateprovence
#### [addressStateProvence]
State or Province in the address of the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[addressStatus]: #addressstatus
#### [addressStatus]
PayPal defined status of the address of the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[addressStreet1]: #addressstreet1
#### [addressStreet1]
First line of the street address of the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[addressStreet2]: #addressstreet2
#### [addressStreet2]
Second line of the street address of the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[contactPhone]: #contactphone
#### [contactPhone]
Phone number provided for the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date that the transaction was attempted.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[exchangeRate]: #exchangerate
#### [exchangeRate]
Exchange rate imposed on the payment amount.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[feeAmount]: #feeamount
#### [feeAmount]
PayPal fee applied to the payment.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[grossAmount]: #grossamount
#### [grossAmount]
The total amount of the payment executed by PayPal, represented in decimal format as US Dollars ($USD).  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique identifier for a single PayPal transaction request.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[invoiceId]: #invoiceid
#### [invoiceId]
Unique identifier of the invoice to which funds will be applied.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[lastPaypalCommand]: #lastpaypalcommand
#### [lastPaypalCommand]
The name of the command issued to PayPal with regards to the attempted transaction.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date that the transaction was modified.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[orderFromIpAddress]: #orderfromipaddress
#### [orderFromIpAddress]
The IP address from where the PayPal payment request originated.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[orderTotal]: #ordertotal
#### [orderTotal]
The amount of the payment submitted through the SoftLayer interface, represented in decimal format as US Dollars ($USD).  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[payer]: #payer
#### [payer]
The PayPal user account name (email address) associated with the customer account.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[payerBusiness]: #payerbusiness
#### [payerBusiness]
The name of the business associated with the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[payerCountry]: #payercountry
#### [payerCountry]
Country given in the address of the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[payerFirstName]: #payerfirstname
#### [payerFirstName]
First name of the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[payerId]: #payerid
#### [payerId]
Unique PayPal user account identifier.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[payerLastName]: #payerlastname
#### [payerLastName]
Last name of the PayPal user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[payerStatus]: #payerstatus
#### [payerStatus]
Current PayPal status associated with the user account.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[paymentDate]: #paymentdate
#### [paymentDate]
Date that the payment was confirmed in PayPal by the user.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[paymentStatus]: #paymentstatus
#### [paymentStatus]
PayPal defined status of the attempted payment.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[paymentType]: #paymenttype
#### [paymentType]
PayPal defined code used to identify the type of payment.  Provided in a PayPal response.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[pendingReason]: #pendingreason
#### [pendingReason]
Reason provided by PayPal for a payment given a pending status.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serializedReply]: #serializedreply
#### [serializedReply]
A serialized, delimited string of the reply received from PayPal.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serializedRequest]: #serializedrequest
#### [serializedRequest]
A serialized, delimited string of the request submitted to PayPal.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[settleAmount]: #settleamount
#### [settleAmount]
PayPal defined fee.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[taxAmount]: #taxamount
#### [taxAmount]
Tax applied by PayPal to the payment amount.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[token]: #token
#### [token]
Value issued by PayPal for referencing the attempted transaction.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[transactionId]: #transactionid
#### [transactionId]
Unique transaction ID provided in a PayPal response.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[transactionType]: #transactiontype
#### [transactionType]
PayPal defined code used to identify the type of transaction.  Provided in a PayPal response.  
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
The account to which a transaction belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[order]: #order
#### [order]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a>**  



</div>

## Count
</div>



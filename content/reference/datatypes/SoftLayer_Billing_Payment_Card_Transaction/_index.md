---
title: "SoftLayer_Billing_Payment_Card_Transaction"
description: "The SoftLayer_Billing_Payment_Card_Transaction data type contains general information relating to attempted credit card... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Payment_Card_Transaction"
---

# SoftLayer_Billing_Payment_Card_Transaction
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_Transaction' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Billing_Payment_Card_Transaction data type contains general information relating to attempted credit card transactions. 





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
The account ID to which the credit card and billing information is associated with.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[amount]: #amount
#### [amount]
The total amount of the attempted transaction, represented in decimal format as US Dollars ($USD).  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[billingAddressLine1]: #billingaddressline1
#### [billingAddressLine1]
The physical street address. Reserve information such as "apartment #123" or "Suite 2" for line 1.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[billingAddressLine2]: #billingaddressline2
#### [billingAddressLine2]
The second line in the address. Information such as suite number goes here.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[billingCity]: #billingcity
#### [billingCity]
The city in which a customer's account resides.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[billingCountryCode]: #billingcountrycode
#### [billingCountryCode]
The 2-character Country code for an account's address. (i.e. US)  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[billingEmail]: #billingemail
#### [billingEmail]
The email address associated with a customer account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[billingNameCompany]: #billingnamecompany
#### [billingNameCompany]
the company name for an account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[billingNameFirst]: #billingnamefirst
#### [billingNameFirst]
The first name of the customer account owner.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[billingNameLast]: #billingnamelast
#### [billingNameLast]
The last name of the customer account owner.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[billingPhoneFax]: #billingphonefax
#### [billingPhoneFax]
The fax number associated with a customer account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[billingPhoneVoice]: #billingphonevoice
#### [billingPhoneVoice]
The phone number associated with a customer account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[billingPostalCode]: #billingpostalcode
#### [billingPostalCode]
The Zip or Postal Code for the billing address on an account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[billingState]: #billingstate
#### [billingState]
The State for the account.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[cardAccountLast4]: #cardaccountlast4
#### [cardAccountLast4]
The last 4 digits of a customer's credit card.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[cardExpirationMonth]: #cardexpirationmonth
#### [cardExpirationMonth]
The month (MM) in which a customer's payment card will expire.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[cardExpirationYear]: #cardexpirationyear
#### [cardExpirationYear]
The year (YYYY) in which a customer's payment card will expire.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[cardType]: #cardtype
#### [cardType]
The type of payment issued (i.e. Visa, MasterCard, American Express).  
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
[id]: #id
#### [id]
The unique identifier for a single credit card transaction request.  
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
[modifyDate]: #modifydate
#### [modifyDate]
The date that the transaction was modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[orderFromIpAddress]: #orderfromipaddress
#### [orderFromIpAddress]
The IP address from which the transaction originates.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[referenceCode]: #referencecode
#### [referenceCode]
A code used by the financial institution to refer to the requested transaction.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[requestId]: #requestid
#### [requestId]
The unique identifier of the request submitted to the financial institution.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[returnStatus]: #returnstatus
#### [returnStatus]
The status code returned from the financial institution.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[serializedReply]: #serializedreply
#### [serializedReply]
A serialized, delimited string of the transaction request sent to the financial institution.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[serializedRequest]: #serializedrequest
#### [serializedRequest]
A serialized, delimited string of the transaction request sent to the financial institution.  
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



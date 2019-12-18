---
title: "SoftLayer_Billing_Payment_Card_ChangeRequest"
description: "The SoftLayer_Billing_Payment_Card_ChangeRequest data type contains general information relating to attempted credit car... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Payment_Card_ChangeRequest"
---

# SoftLayer_Billing_Payment_Card_ChangeRequest
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_ChangeRequest' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Billing_Payment_Card_ChangeRequest data type contains general information relating to attempted credit card information changes. 





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
The account ID to which the credit card and billing information is associated with.  
<span class="type-label">Type: </span>**integer**

-----
[amount]: #amount
#### [amount]
The total amount of the attempted transaction, represented in decimal format as US Dollars ($USD).  
<span class="type-label">Type: </span>**decimal**

-----
[billingAddressLine1]: #billingaddressline1
#### [billingAddressLine1]
The physical street address. Reserve information such as "apartment #123" or "Suite 2" for line 1.  
<span class="type-label">Type: </span>**string**

-----
[billingAddressLine2]: #billingaddressline2
#### [billingAddressLine2]
The second line in the address. Information such as suite number goes here.  
<span class="type-label">Type: </span>**string**

-----
[billingCity]: #billingcity
#### [billingCity]
The city in which a customer's account resides.  
<span class="type-label">Type: </span>**string**

-----
[billingCountryCode]: #billingcountrycode
#### [billingCountryCode]
The 2-character Country code for an account's address. (i.e. US)  
<span class="type-label">Type: </span>**string**

-----
[billingEmail]: #billingemail
#### [billingEmail]
The email address associated with a customer account.  
<span class="type-label">Type: </span>**string**

-----
[billingNameCompany]: #billingnamecompany
#### [billingNameCompany]
the company name for an account.  
<span class="type-label">Type: </span>**string**

-----
[billingNameFirst]: #billingnamefirst
#### [billingNameFirst]
The first name of the customer account owner.  
<span class="type-label">Type: </span>**string**

-----
[billingNameLast]: #billingnamelast
#### [billingNameLast]
The last name of the customer account owner  
<span class="type-label">Type: </span>**string**

-----
[billingPhoneFax]: #billingphonefax
#### [billingPhoneFax]
The fax number associated with a customer account.  
<span class="type-label">Type: </span>**string**

-----
[billingPhoneVoice]: #billingphonevoice
#### [billingPhoneVoice]
The phone number associated with a customer account.  
<span class="type-label">Type: </span>**string**

-----
[billingPostalCode]: #billingpostalcode
#### [billingPostalCode]
The Zip or Postal Code for the billing address on an account.  
<span class="type-label">Type: </span>**string**

-----
[billingState]: #billingstate
#### [billingState]
The State for the account.  
<span class="type-label">Type: </span>**string**

-----
[cardAccountLast4]: #cardaccountlast4
#### [cardAccountLast4]
The last 4 digits of a customer's credit card.  
<span class="type-label">Type: </span>**string**

-----
[cardAccountNumber]: #cardaccountnumber
#### [cardAccountNumber]
The card number submitted in the change request.  
<span class="type-label">Type: </span>**string**

-----
[cardExpirationMonth]: #cardexpirationmonth
#### [cardExpirationMonth]
The month (MM) in which a customer's payment card will expire.  
<span class="type-label">Type: </span>**string**

-----
[cardExpirationYear]: #cardexpirationyear
#### [cardExpirationYear]
The year (YYYY) in which a customer's payment card will expire.  
<span class="type-label">Type: </span>**string**

-----
[cardNickname]: #cardnickname
#### [cardNickname]
  
<span class="type-label">Type: </span>**string**

-----
[cardType]: #cardtype
#### [cardType]
The type of payment card a customer has. (i.e. Visa, MasterCard, American Express).  
<span class="type-label">Type: </span>**string**

-----
[creditCardVerificationNumber]: #creditcardverificationnumber
#### [creditCardVerificationNumber]
The credit card verification number submitted in the change request.  
<span class="type-label">Type: </span>**string**

-----
[currencyShortName]: #currencyshortname
#### [currencyShortName]
Describes the currency selected for payment  
<span class="type-label">Type: </span>**string**

-----
[deviceFingerprintId]: #devicefingerprintid
#### [deviceFingerprintId]
Device Fingerprint Identifier - Used internally and can safely be ignored.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
The unique identifier for a single change request.  
<span class="type-label">Type: </span>**integer**

-----
[notes]: #notes
#### [notes]
the notes stored about a customer's payment card.  
<span class="type-label">Type: </span>**string**

-----
[paymentRoleId]: #paymentroleid
#### [paymentRoleId]
  
<span class="type-label">Type: </span>**integer**

-----
[paymentType]: #paymenttype
#### [paymentType]
The description of the type of payment sent in a change transaction.  
<span class="type-label">Type: </span>**string**

-----
[ticketId]: #ticketid
#### [ticketId]
Unique identifier for a ticket discussing the switch between payment methods.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[authorizedCreditCardTransaction]: #authorizedcreditcardtransaction
#### [authorizedCreditCardTransaction]
The SoftLayer_Billing_Payment_Card_Transaction tied to the authorization performed as part of this change request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_Transaction'>SoftLayer_Billing_Payment_Card_Transaction </a>**

-----
[captureCreditCardTransaction]: #capturecreditcardtransaction
#### [captureCreditCardTransaction]
The SoftLayer_Billing_Payment_Card_Transaction tied to the capture of funds performed as part of this change request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_Transaction'>SoftLayer_Billing_Payment_Card_Transaction </a>**

-----
[ticketAttachmentReferences]: #ticketattachmentreferences
#### [ticketAttachmentReferences]
These are tickets tied to a credit card change request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Attachment'>SoftLayer_Ticket_Attachment[] </a>**


## Count

-----
[ticketAttachmentReferenceCount]: #ticketattachmentreferencecount
#### [ticketAttachmentReferenceCount]
A count of these are tickets tied to a credit card change request.   
<span class="type-label">Type: </span>**unsigned long**

</div>



---
title: "SoftLayer_Billing_Info"
description: "Every SoftLayer customer account has billing specific information which is kept in the SoftLayer_Billing_Info data type.... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Info"
---

# SoftLayer_Billing_Info
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Info' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Info' >Datatype</a></li>
    </ul>
</div>

## Description 
Every SoftLayer customer account has billing specific information which is kept in the SoftLayer_Billing_Info data type. This information is used by the SoftLayer accounting group when sending invoices and making billing inquiries. 


### associatedMethods

*  [SoftLayer_Account::getBillingInfo](/reference/services/SoftLayer_Account/getBillingInfo )





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
A SoftLayer account's identifier.  
<span class="type-label">Type: </span>**integer**

-----
[anniversaryDayOfMonth]: #anniversarydayofmonth
#### [anniversaryDayOfMonth]
The day of the month that a SoftLayer customer is billed.  
<span class="type-label">Type: </span>**integer**

-----
[cardAccountNumber]: #cardaccountnumber
#### [cardAccountNumber]
This value doesn't persist to this object. It's used as part of the account creation process only;  
<span class="type-label">Type: </span>**string**

-----
[cardExpirationMonth]: #cardexpirationmonth
#### [cardExpirationMonth]
the expiration month of the credit card on file  
<span class="type-label">Type: </span>**integer**

-----
[cardExpirationYear]: #cardexpirationyear
#### [cardExpirationYear]
the expiration year of the credit card on file  
<span class="type-label">Type: </span>**integer**

-----
[cardNickname]: #cardnickname
#### [cardNickname]
  
<span class="type-label">Type: </span>**string**

-----
[cardType]: #cardtype
#### [cardType]
the type of the credit card on file  
<span class="type-label">Type: </span>**string**

-----
[cardVerificationNumber]: #cardverificationnumber
#### [cardVerificationNumber]
This value doesn't persist to this object. It's used as part of the account creation process only.  
<span class="type-label">Type: </span>**string**

-----
[createDate]: #createdate
#### [createDate]
The date a customer's billing information was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
A SoftLayer customer's billing information identifier.  
<span class="type-label">Type: </span>**integer**

-----
[lastFourPaymentCardDigits]: #lastfourpaymentcarddigits
#### [lastFourPaymentCardDigits]
The last four digits of the credit card currently on the account. This is the only portion of the card that we store. For Paypal customers, this value will be empty.  
<span class="type-label">Type: </span>**integer**

-----
[lastPaymentDate]: #lastpaymentdate
#### [lastPaymentDate]
The date of the last payment received by SoftLayer from the account holder.  
<span class="type-label">Type: </span>**dateTime**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a customer's billing information was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[paymentTerms]: #paymentterms
#### [paymentTerms]
The payment terms for an account.  
<span class="type-label">Type: </span>**integer**

-----
[percentDiscountOnetime]: #percentdiscountonetime
#### [percentDiscountOnetime]
The percentage discount received on all one-time charges on a customer's monthly bill.  
<span class="type-label">Type: </span>**integer**

-----
[percentDiscountRecurring]: #percentdiscountrecurring
#### [percentDiscountRecurring]
The percentage discount received on all recurring charges on a customer's monthly bill.  
<span class="type-label">Type: </span>**integer**

-----
[sparePoolAmount]: #sparepoolamount
#### [sparePoolAmount]
The total recurring fee amount for servers that are in the spare pool status.  
<span class="type-label">Type: </span>**integer**

-----
[taxCertificateId]: #taxcertificateid
#### [taxCertificateId]
  
<span class="type-label">Type: </span>**string**

-----
[vatId]: #vatid
#### [vatId]
  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The SoftLayer customer account associated with this billing information.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[achInformation]: #achinformation
#### [achInformation]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Info_Ach'>SoftLayer_Billing_Info_Ach[] </a>**

-----
[currency]: #currency
#### [currency]
Currency to be used by this customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Currency'>SoftLayer_Billing_Currency </a>**

-----
[currentBillingCycle]: #currentbillingcycle
#### [currentBillingCycle]
Information related to an account's current and previous billing cycles.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Info_Cycle'>SoftLayer_Billing_Info_Cycle </a>**

-----
[lastBillDate]: #lastbilldate
#### [lastBillDate]
The date on which an account was last billed.  
<span class="type-label">Type: </span>**dateTime**

-----
[nextBillDate]: #nextbilldate
#### [nextBillDate]
The date on which an account will be billed next.  
<span class="type-label">Type: </span>**dateTime**


## Count

-----
[achInformationCount]: #achinformationcount
#### [achInformationCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>



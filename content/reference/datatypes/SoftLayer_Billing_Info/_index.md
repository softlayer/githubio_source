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
A SoftLayer account's identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[anniversaryDayOfMonth]: #anniversarydayofmonth
#### [anniversaryDayOfMonth]
The day of the month that a SoftLayer customer is billed.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[cardAccountNumber]: #cardaccountnumber
#### [cardAccountNumber]
This value doesn't persist to this object. It's used as part of the account creation process only;  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[cardExpirationMonth]: #cardexpirationmonth
#### [cardExpirationMonth]
the expiration month of the credit card on file  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[cardExpirationYear]: #cardexpirationyear
#### [cardExpirationYear]
the expiration year of the credit card on file  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[cardNickname]: #cardnickname
#### [cardNickname]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[cardType]: #cardtype
#### [cardType]
the type of the credit card on file  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[cardVerificationNumber]: #cardverificationnumber
#### [cardVerificationNumber]
This value doesn't persist to this object. It's used as part of the account creation process only.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date a customer's billing information was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A SoftLayer customer's billing information identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[lastFourPaymentCardDigits]: #lastfourpaymentcarddigits
#### [lastFourPaymentCardDigits]
The last four digits of the credit card currently on the account. This is the only portion of the card that we store. For Paypal customers, this value will be empty.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[lastPaymentDate]: #lastpaymentdate
#### [lastPaymentDate]
The date of the last payment received by SoftLayer from the account holder.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a customer's billing information was last modified.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[paymentTerms]: #paymentterms
#### [paymentTerms]
The payment terms for an account.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[percentDiscountOnetime]: #percentdiscountonetime
#### [percentDiscountOnetime]
The percentage discount received on all one-time charges on a customer's monthly bill.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[percentDiscountRecurring]: #percentdiscountrecurring
#### [percentDiscountRecurring]
The percentage discount received on all recurring charges on a customer's monthly bill.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[sparePoolAmount]: #sparepoolamount
#### [sparePoolAmount]
The total recurring fee amount for servers that are in the spare pool status.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[taxCertificateId]: #taxcertificateid
#### [taxCertificateId]
This property has been deprecated.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[vatId]: #vatid
#### [vatId]
  
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
The SoftLayer customer account associated with this billing information.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[achInformation]: #achinformation
#### [achInformation]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Info_Ach'>SoftLayer_Billing_Info_Ach[] </a>**  



</div>
<div class="prop-row">

-----
[currency]: #currency
#### [currency]
Currency to be used by this customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Currency'>SoftLayer_Billing_Currency </a>**  



</div>
<div class="prop-row">

-----
[currentBillingCycle]: #currentbillingcycle
#### [currentBillingCycle]
Information related to an account's current and previous billing cycles.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Info_Cycle'>SoftLayer_Billing_Info_Cycle </a>**  



</div>
<div class="prop-row">

-----
[lastBillDate]: #lastbilldate
#### [lastBillDate]
The date on which an account was last billed.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[nextBillDate]: #nextbilldate
#### [nextBillDate]
The date on which an account will be billed next.  
<span class="type-label">Type: </span>**dateTime**  



</div>

## Count
<div class="prop-row">

-----
[achInformationCount]: #achinformationcount
#### [achInformationCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>



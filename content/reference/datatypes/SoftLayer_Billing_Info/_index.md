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
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Info' >Datatype</a></li>
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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#accountId" name=accountId>accountId</a></span>
            <div class='views-field-body'>A SoftLayer account's identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#anniversaryDayOfMonth" name=anniversaryDayOfMonth>anniversaryDayOfMonth</a></span>
            <div class='views-field-body'>The day of the month that a SoftLayer customer is billed. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardAccountNumber" name=cardAccountNumber>cardAccountNumber</a></span>
            <div class='views-field-body'>This value doesn't persist to this object. It's used as part of the account creation process only; </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardExpirationMonth" name=cardExpirationMonth>cardExpirationMonth</a></span>
            <div class='views-field-body'>the expiration month of the credit card on file </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardExpirationYear" name=cardExpirationYear>cardExpirationYear</a></span>
            <div class='views-field-body'>the expiration year of the credit card on file </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardNickname" name=cardNickname>cardNickname</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardType" name=cardType>cardType</a></span>
            <div class='views-field-body'>the type of the credit card on file </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardVerificationNumber" name=cardVerificationNumber>cardVerificationNumber</a></span>
            <div class='views-field-body'>This value doesn't persist to this object. It's used as part of the account creation process only. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date a customer's billing information was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A SoftLayer customer's billing information identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lastFourPaymentCardDigits" name=lastFourPaymentCardDigits>lastFourPaymentCardDigits</a></span>
            <div class='views-field-body'>The last four digits of the credit card currently on the account. This is the only portion of the card that we store. For Paypal customers, this value will be empty. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lastPaymentDate" name=lastPaymentDate>lastPaymentDate</a></span>
            <div class='views-field-body'>The date of the last payment received by SoftLayer from the account holder. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date a customer's billing information was last modified. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#paymentTerms" name=paymentTerms>paymentTerms</a></span>
            <div class='views-field-body'>The payment terms for an account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#percentDiscountOnetime" name=percentDiscountOnetime>percentDiscountOnetime</a></span>
            <div class='views-field-body'>The percentage discount received on all one-time charges on a customer's monthly bill. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#percentDiscountRecurring" name=percentDiscountRecurring>percentDiscountRecurring</a></span>
            <div class='views-field-body'>The percentage discount received on all recurring charges on a customer's monthly bill. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sparePoolAmount" name=sparePoolAmount>sparePoolAmount</a></span>
            <div class='views-field-body'>The total recurring fee amount for servers that are in the spare pool status. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#vatId" name=vatId>vatId</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The SoftLayer customer account associated with this billing information. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#achInformation" name=achInformation>achInformation</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Info_Ach'>SoftLayer_Billing_Info_Ach[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#currency" name=currency>currency</a></span>
            <div class='views-field-body'>Currency to be used by this customer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Currency'>SoftLayer_Billing_Currency </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#currentBillingCycle" name=currentBillingCycle>currentBillingCycle</a></span>
            <div class='views-field-body'>Information related to an account's current and previous billing cycles. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Info_Cycle'>SoftLayer_Billing_Info_Cycle </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lastBillDate" name=lastBillDate>lastBillDate</a></span>
            <div class='views-field-body'>The date on which an account was last billed. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#nextBillDate" name=nextBillDate>nextBillDate</a></span>
            <div class='views-field-body'>The date on which an account will be billed next. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#achInformationCount" name=achInformationCount>achInformationCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>



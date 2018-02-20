---
title: "SoftLayer_Billing_Payment_Card_ManualPayment"
description: "The SoftLayer_Billing_Payment_Card_ManualPayment data type contains general information relating to attempted credit car... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Payment_Card_ManualPayment"
---

# SoftLayer_Billing_Payment_Card_ManualPayment
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_ManualPayment' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Billing_Payment_Card_ManualPayment data type contains general information relating to attempted credit card information changes. 
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
            <div class='views-field-body'>The account ID to which the credit card and billing information is associated with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#amount" name=amount>amount</a></span>
            <div class='views-field-body'>The total amount of the attempted transaction, represented in decimal format as US Dollars ($USD). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#authorizedCreditCardTransactionId" name=authorizedCreditCardTransactionId>authorizedCreditCardTransactionId</a></span>
            <div class='views-field-body'>The unique identifier of an attempted credit card transaction. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#authorizedPayPalTransactionId" name=authorizedPayPalTransactionId>authorizedPayPalTransactionId</a></span>
            <div class='views-field-body'>The unique identifier of an attempted PayPal transaction. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingAddressLine1" name=billingAddressLine1>billingAddressLine1</a></span>
            <div class='views-field-body'>The physical street address. Reserve information such as "apartment #123" or "Suite 2" for line 1. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingAddressLine2" name=billingAddressLine2>billingAddressLine2</a></span>
            <div class='views-field-body'>The second line in the address. Information such as suite number goes here. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingCity" name=billingCity>billingCity</a></span>
            <div class='views-field-body'>The city in which a customer's account resides. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingCountryCode" name=billingCountryCode>billingCountryCode</a></span>
            <div class='views-field-body'>The 2-character Country code for an account's address. (i.e. US) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingEmail" name=billingEmail>billingEmail</a></span>
            <div class='views-field-body'>The email address associated with a customer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingNameCompany" name=billingNameCompany>billingNameCompany</a></span>
            <div class='views-field-body'>the company name for an account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingNameFirst" name=billingNameFirst>billingNameFirst</a></span>
            <div class='views-field-body'>The first name of the customer account owner. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingNameLast" name=billingNameLast>billingNameLast</a></span>
            <div class='views-field-body'>The last name of the customer account owner. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingPhoneFax" name=billingPhoneFax>billingPhoneFax</a></span>
            <div class='views-field-body'>The fax number associated with a customer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingPhoneVoice" name=billingPhoneVoice>billingPhoneVoice</a></span>
            <div class='views-field-body'>The phone number associated with a customer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingPostalCode" name=billingPostalCode>billingPostalCode</a></span>
            <div class='views-field-body'>The Zip or Postal Code for the billing address on an account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingState" name=billingState>billingState</a></span>
            <div class='views-field-body'>The State for the account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cancelUrl" name=cancelUrl>cancelUrl</a></span>
            <div class='views-field-body'>The cancel URL is the page to which PayPal redirects if payment is not approved. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardAccountHash" name=cardAccountHash>cardAccountHash</a></span>
            <div class='views-field-body'>A hash value of the credit card number. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardAccountLast4" name=cardAccountLast4>cardAccountLast4</a></span>
            <div class='views-field-body'>The last 4 digits of a customer's credit card. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardAccountNumber" name=cardAccountNumber>cardAccountNumber</a></span>
            <div class='views-field-body'>The card number submitted in the change request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardExpirationMonth" name=cardExpirationMonth>cardExpirationMonth</a></span>
            <div class='views-field-body'>The month (MM) in which a customer's payment card will expire. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardExpirationYear" name=cardExpirationYear>cardExpirationYear</a></span>
            <div class='views-field-body'>The year (YYYY) in which a customer's payment card will expire. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardType" name=cardType>cardType</a></span>
            <div class='views-field-body'>The method key of the type payment issued (Visa - 001, Mastercard - 002, American Express - 003, Discover - 004, PayPal - paypal). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#creditCardVerificationNumber" name=creditCardVerificationNumber>creditCardVerificationNumber</a></span>
            <div class='views-field-body'>The credit card verification number submitted in the change request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#currencyShortName" name=currencyShortName>currencyShortName</a></span>
            <div class='views-field-body'>Describes the currency selected for payment </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deviceFingerprintId" name=deviceFingerprintId>deviceFingerprintId</a></span>
            <div class='views-field-body'>Device Fingerprint Identifier - Used internally and can safely be ignored. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#fromIpAddress" name=fromIpAddress>fromIpAddress</a></span>
            <div class='views-field-body'>The IP address from which the transaction originates. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique identifier for a single manual payment request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notes" name=notes>notes</a></span>
            <div class='views-field-body'>Notes generated as a result of the payment request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#paymentType" name=paymentType>paymentType</a></span>
            <div class='views-field-body'>The description of the type of payment sent in a change transaction. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#returnUrl" name=returnUrl>returnUrl</a></span>
            <div class='views-field-body'>The return URL is the page to which PayPal redirects after payment is approved. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>Describes the type of manual payment (PAYPAL or CREDIT_CARD). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#authorizedCreditCardTransaction" name=authorizedCreditCardTransaction>authorizedCreditCardTransaction</a></span>
            <div class='views-field-body'>This is the credit card transaction data tied to a credit card manual payment. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_Transaction'>SoftLayer_Billing_Payment_Card_Transaction </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#authorizedPayPalTransaction" name=authorizedPayPalTransaction>authorizedPayPalTransaction</a></span>
            <div class='views-field-body'>This is the PayPal transaction data tied to a PayPal manual payment. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Payment_PayPal_Transaction'>SoftLayer_Billing_Payment_PayPal_Transaction </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#captureCreditCardTransaction" name=captureCreditCardTransaction>captureCreditCardTransaction</a></span>
            <div class='views-field-body'>The SoftLayer_Billing_Payment_Card_Transaction tied to the capture performed as part of this manual payment. This will only exist if the manual payment was performed with a credit card. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_Transaction'>SoftLayer_Billing_Payment_Card_Transaction </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#capturePayPalTransaction" name=capturePayPalTransaction>capturePayPalTransaction</a></span>
            <div class='views-field-body'>The SoftLayer_Billing_Payment_PayPal_Transaction tied to the capture performed as part of this manual payment. This will only exist if the manual payment was performed via PayPal. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Payment_PayPal_Transaction'>SoftLayer_Billing_Payment_PayPal_Transaction </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ticketAttachmentReferences" name=ticketAttachmentReferences>ticketAttachmentReferences</a></span>
            <div class='views-field-body'>These are tickets tied to a credit card manual payment. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket_Attachment'>SoftLayer_Ticket_Attachment[] </a></p></div>
        </div>
            </div>
</div>



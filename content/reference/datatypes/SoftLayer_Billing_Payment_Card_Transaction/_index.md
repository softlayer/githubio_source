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
            <span class='views-field-title'><a href="#cardAccountLast4" name=cardAccountLast4>cardAccountLast4</a></span>
            <div class='views-field-body'>The last 4 digits of a customer's credit card. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardExpirationMonth" name=cardExpirationMonth>cardExpirationMonth</a></span>
            <div class='views-field-body'>The month (MM) in which a customer's payment card will expire. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardExpirationYear" name=cardExpirationYear>cardExpirationYear</a></span>
            <div class='views-field-body'>The year (YYYY) in which a customer's payment card will expire. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cardType" name=cardType>cardType</a></span>
            <div class='views-field-body'>The type of payment issued (i.e. Visa, MasterCard, American Express). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date that the transaction was attempted. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique identifier for a single credit card transaction request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#invoiceId" name=invoiceId>invoiceId</a></span>
            <div class='views-field-body'>Unique identifier of the invoice to which funds will be applied. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date that the transaction was modified. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderFromIpAddress" name=orderFromIpAddress>orderFromIpAddress</a></span>
            <div class='views-field-body'>The IP address from which the transaction originates. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#referenceCode" name=referenceCode>referenceCode</a></span>
            <div class='views-field-body'>A code used by the financial institution to refer to the requested transaction. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#requestId" name=requestId>requestId</a></span>
            <div class='views-field-body'>The unique identifier of the request submitted to the financial institution. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#returnStatus" name=returnStatus>returnStatus</a></span>
            <div class='views-field-body'>The status code returned from the financial institution. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serializedReply" name=serializedReply>serializedReply</a></span>
            <div class='views-field-body'>A serialized, delimited string of the transaction request sent to the financial institution. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serializedRequest" name=serializedRequest>serializedRequest</a></span>
            <div class='views-field-body'>A serialized, delimited string of the transaction request sent to the financial institution. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The account to which a transaction belongs. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#order" name=order>order</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a></p></div>
        </div>
            </div>
</div>



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
            <div class='views-field-body'>The account ID to which the PayPal and billing information is associated with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#addressCityName" name=addressCityName>addressCityName</a></span>
            <div class='views-field-body'>City given in the address of the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#addressCountry" name=addressCountry>addressCountry</a></span>
            <div class='views-field-body'>Country given in the named address of the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#addressName" name=addressName>addressName</a></span>
            <div class='views-field-body'>Name given to the address provided for the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#addressPostalCode" name=addressPostalCode>addressPostalCode</a></span>
            <div class='views-field-body'>Postal Code of the address of the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#addressStateProvence" name=addressStateProvence>addressStateProvence</a></span>
            <div class='views-field-body'>State or Province in the address of the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#addressStatus" name=addressStatus>addressStatus</a></span>
            <div class='views-field-body'>PayPal defined status of the address of the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#addressStreet1" name=addressStreet1>addressStreet1</a></span>
            <div class='views-field-body'>First line of the street address of the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#addressStreet2" name=addressStreet2>addressStreet2</a></span>
            <div class='views-field-body'>Second line of the street address of the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#contactPhone" name=contactPhone>contactPhone</a></span>
            <div class='views-field-body'>Phone number provided for the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date that the transaction was attempted. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#exchangeRate" name=exchangeRate>exchangeRate</a></span>
            <div class='views-field-body'>Exchange rate imposed on the payment amount. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#feeAmount" name=feeAmount>feeAmount</a></span>
            <div class='views-field-body'>PayPal fee applied to the payment. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#grossAmount" name=grossAmount>grossAmount</a></span>
            <div class='views-field-body'>The total amount of the payment executed by PayPal, represented in decimal format as US Dollars ($USD). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique identifier for a single PayPal transaction request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#invoiceId" name=invoiceId>invoiceId</a></span>
            <div class='views-field-body'>Unique identifier of the invoice to which funds will be applied. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lastPaypalCommand" name=lastPaypalCommand>lastPaypalCommand</a></span>
            <div class='views-field-body'>The name of the command issued to PayPal with regards to the attempted transaction. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date that the transaction was modified. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderFromIpAddress" name=orderFromIpAddress>orderFromIpAddress</a></span>
            <div class='views-field-body'>The IP address from where the PayPal payment request originated. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderTotal" name=orderTotal>orderTotal</a></span>
            <div class='views-field-body'>The amount of the payment submitted through the SoftLayer interface, represented in decimal format as US Dollars ($USD). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#payer" name=payer>payer</a></span>
            <div class='views-field-body'>The PayPal user account name (email address) associated with the customer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#payerBusiness" name=payerBusiness>payerBusiness</a></span>
            <div class='views-field-body'>The name of the business associated with the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#payerCountry" name=payerCountry>payerCountry</a></span>
            <div class='views-field-body'>Country given in the address of the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#payerFirstName" name=payerFirstName>payerFirstName</a></span>
            <div class='views-field-body'>First name of the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#payerId" name=payerId>payerId</a></span>
            <div class='views-field-body'>Unique PayPal user account identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#payerLastName" name=payerLastName>payerLastName</a></span>
            <div class='views-field-body'>Last name of the PayPal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#payerStatus" name=payerStatus>payerStatus</a></span>
            <div class='views-field-body'>Current PayPal status associated with the user account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#paymentDate" name=paymentDate>paymentDate</a></span>
            <div class='views-field-body'>Date that the payment was confirmed in PayPal by the user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#paymentStatus" name=paymentStatus>paymentStatus</a></span>
            <div class='views-field-body'>PayPal defined status of the attempted payment. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#paymentType" name=paymentType>paymentType</a></span>
            <div class='views-field-body'>PayPal defined code used to identify the type of payment.  Provided in a PayPal response. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#pendingReason" name=pendingReason>pendingReason</a></span>
            <div class='views-field-body'>Reason provided by PayPal for a payment given a pending status. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serializedReply" name=serializedReply>serializedReply</a></span>
            <div class='views-field-body'>A serialized, delimited string of the reply received from PayPal. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serializedRequest" name=serializedRequest>serializedRequest</a></span>
            <div class='views-field-body'>A serialized, delimited string of the request submitted to PayPal. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#settleAmount" name=settleAmount>settleAmount</a></span>
            <div class='views-field-body'>PayPal defined fee. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#taxAmount" name=taxAmount>taxAmount</a></span>
            <div class='views-field-body'>Tax applied by PayPal to the payment amount. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#token" name=token>token</a></span>
            <div class='views-field-body'>Value issued by PayPal for referencing the attempted transaction. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#transactionId" name=transactionId>transactionId</a></span>
            <div class='views-field-body'>Unique transaction ID provided in a PayPal response. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#transactionType" name=transactionType>transactionType</a></span>
            <div class='views-field-body'>PayPal defined code used to identify the type of transaction.  Provided in a PayPal response. </div>
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
                <h2>Relational</h2>
            </div>
</div>



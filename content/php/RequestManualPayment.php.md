---
title: "RequestManualPayment.php"
description: "RequestManualPayment.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Payment_Card_ManualPayment"
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
tags:
    - "account"
---


```
<?php
/**
 * Make a Payment
 *
 * This script makes a manual payment. Softlayer customers are permitted to request a manual
 * one-time payment at a minimum amount of $2.00.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/requestManualPayment
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Payment_Card_ManualPayment
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once dirname(__FILE__) . "/SoftLayer/SoapClient.class.php";

/**
 * SoftLayer API username
 * @var string
 */
$username = 'set me';

/**
 * SoftLayer API key
 * @var string
 */
$apiKey = 'set me';

/**
 * Declare parameters for Payment Information
 * @var Decimal $amount
 */
$amount = 50.55;

/**
 * Declare Credit Card Payment information
 * @var String $cardAccountNumber
 * @var String $cardExpirationMonth
 * @var String $cardExpirationYear
 * @var String $cardType
 * @var String $creditCardVerificationNumber
 * @var String $currencyShortName
 * @var String $paymentType
 */
$cardAccountNumber = "4111111111111111";
$cardExpirationMonth = "10";
$cardExpirationYear = "2017";
// $cardType : Visa - 001, Mastercard - 002, American Express - 003, Discover - 004, PayPal - paypal
$cardType = "001";
$creditCardVerificationNumber = "1111";
$currencyShortName = "USD";
// $paymentType : The description of the type of payment sent.
$paymentType = "cc";

/**
 * Declare Credit Card Billing Addres information
 * @var String $billingAddressLine1
 * @var String $billingAddressLine2
 * @var String $billingCity
 * @var String $billingCountryCode
 * @var String $billingEmail
 * @var String $billingNameCompany
 * @var String $billingNameFirst
 * @var String $billingNameLast
 * @var String $billingPhoneVoice
 * @var String $billingPostalCode
 * @var String $billingState
 */
$billingAddressLine1 = "Test";
$billingAddressLine2 = "";
$billingCity = "Cbba";
$billingCountryCode = "US";
$billingEmail = "noreply@softlayer.com";
$billingNameCompany = "TestCompany";
$billingNameFirst = "Jhon";
$billingNameLast = "Thoms";
$billingPhoneVoice = "2342342";
$billingPostalCode = "44559";
$billingState = "TX";

// Build a SoftLayer_Billing_Payment_Card_ManualPayment object containing
// the details required to request a manual payment.
$request = new stdClass();
$request -> amount = $amount;
$request -> billingAddressLine1 = $billingAddressLine1;
$request -> billingCity = $billingCity;
$request -> billingCountryCode = $billingCountryCode;
$request -> billingEmail = $billingEmail;
$request -> billingNameCompany = $billingNameCompany;
$request -> billingNameFirst = $billingNameFirst;
$request -> billingNameLast = $billingNameLast;
$request -> billingPhoneVoice = $billingPhoneVoice;
$request -> billingPostalCode = $billingPostalCode;
$request -> billingState = $billingState;
$request -> cardAccountNumber = $cardAccountNumber;
$request -> cardExpirationMonth = $cardExpirationMonth;
$request -> cardExpirationYear = $cardExpirationYear;
$request -> cardType = $cardType;
$request -> creditCardVerificationNumber = $creditCardVerificationNumber;
$request -> currencyShortName = $currencyShortName;
$request -> paymentType = $paymentType;
$request -> billingPostalCode = $billingPostalCode;

// Create SoftLayer API client object
$client = SoftLayer_SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);

try {
    $receipt = $client -> requestManualPayment($request);
    print_r($receipt);
} catch(Exception $e) {
    echo "Unable to request manual payment: " . $e -> getMessage();
}

```

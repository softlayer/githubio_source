---
title: "RequestManualPaymentUsingCreditCardOnFile.php"
description: "RequestManualPaymentUsingCreditCardOnFile.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Payment_Card_ManualPayment"
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
tags:
    - "account"
---


```php
<?php
/**
 * This script makes a Manual Payment Request for a manual payment using a credit card which is on 
 * file and does not require an approval process.
 * SoftLayer customers are permitted to request a manual one-time payment at a minimum amount of $2.00
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/requestManualPaymentUsingCreditCardOnFile
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
$amount = 10.00;

/**
 * Declare pay with alternate card flag
 * @var Boolean $payWithAlternateCardFlag
 */
$payWithAlternateCardFlag = false;

/**
 * Declare optional note which will be added to the manual payment request
 * @var String note
 */
$note = "This is for test";

// Create SoftLayer API client object
$client = SoftLayer_SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);

try {
    $receipt = $client -> requestManualPaymentUsingCreditCardOnFile($amount, $payWithAlternateCardFlag, $note);
    print_r($receipt);
} catch(Exception $e) {
    echo "Unable to request manual payment using credit card on file: " . $e -> getMessage();
}

```

---
title: "GetInvoices.php"
description: "GetInvoices.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Invoice"
tags:
    - "billing"
---


```
<?php
/**
* Retrieve the invoice information.
*
* This script makes a single call to the getInvoices() method in the
* SoftLayer_Account API service and uses a object mask to get more
* information about the invoices.
*
* Important manual pages
* http://sldn.softlayer.com/reference/services/SoftLayer_Account
* http://sldn.softlayer.com/reference/services/SoftLayer_Account/getInvoices
* http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Invoice
* 
* License: http:'sldn.softlayer.com/article/License
* Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
require_once ('C:/scripst/getdetails/SoftLayer/SoapClient.class.php');

// Client configuration
// Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

// Declaring the API client
$accountService = Softlayer_SoapClient::getClient('SoftLayer_Account', null, $apiUsername, $apiKey);

// Declaring the object mask to get information about the billing item.
$objectMask = 'mask[payment,amount,invoiceTotalOneTimeAmount,invoiceTotalRecurringAmount,invoiceTotalOneTimeTaxAmount,invoiceTotalRecurringTaxAmount]';
$accountService->setObjectMask($objectMask);

try {
    // Retrieving the invoices for the account.
    $invoices = $accountService->getInvoices();
    print_r($invoices);
} catch (Exception $e) {
    die('Unable to retrieve the invoices. ' . $e->getMessage());

}
?>

```

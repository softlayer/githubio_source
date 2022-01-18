---
title: "Cancel an item or service"
description: "Use cancelService to cancel am item or service."
date: "2016-01-29"
classes: ["SoftLayer_Billing_Item"]
tags:
    - "cancelservice"
    - "billing"
---

In order to cancel an item or service you must know the billing item ID. In the following example we are retrieving the billing item ID for our Virtual Guest with ID '15690533':

```php
<?php

require_once './vendor/autoload.php';
$apiUsername = '';
$apiKey = '';
$itemId = '15690533'; # ID of the service or item you want to get the billing ID of
$invokeService = 'SoftLayer_Virtual_Guest';

try {
     $billingItemClient = \SoftLayer\SoapClient::getClient($invokeService, $itemId, $apiUsername, $apiKey);
     $result = $billingItemClient->getBillingItem();
     print_r($result);

 } catch(Exception $e) {
     echo 'Unable to get billing ID from the item: ' . $e->getMessage();
 }

?>
```

Once we have the billing item ID we can plug it in to the cancelservice code:

```php
<?php

require_once './vendor/autoload.php';
$apiUsername = '';
$apiKey = '';
$billingitemId = '1234567'; # Billing ID of the service or item you want to cancel obtained from the previous example
$billingItemService = 'SoftLayer_Billing_Item';

try {
     $billingItemClient = \SoftLayer\SoapClient::getClient($billingItemService, $itemId, $apiUsername, $apiKey);
     $result = $billingItemClient->cancelService();
     print_r($result);

 } catch(Exception $e) {
     echo 'Unable to cancel the item: ' . $e->getMessage();
 }

?>
```

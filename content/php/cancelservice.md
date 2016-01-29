---
title: "Cancel an item or service"
description: "Use cancelService to cancel am item or service."
date: "2016-01-29"
classes: ["SoftLayer_Billing_Item"]
tags:
    - "cancelService"
    - "billing"
---


```php
<?php

require_once './vendor/autoload.php';
$apiUsername = '';
$apiKey = '';
$itemId = '1234567'; # Billing ID of the service or item you want to cancel
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

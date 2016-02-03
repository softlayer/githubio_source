---
title: "Month-to-date cost of a Virtual_Guest"
description: "Determine the month-to-date cost of an hourly Virtual_Guest using getBillingItem and an objectMask."
date: "2016-01-29"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "objectMask"
    - "billing"
---


```php
<?php

require_once './vendor/autoload.php';
$apiUsername = '';
$apiKey = '';
$guest = '1234567'; # Put your VSI ID here

$client = \SoftLayer\SoapClient::getClient('SoftLayer_Virtual_Guest', $guest, $apiUsername, $apiKey);
$objectMask = new \SoftLayer\Common\ObjectMask();
$objectMask->createDate;
$objectMask->hoursUsed;
$objectMask->hourlyRecurringFee;
$objectMask->currentHourlyCharge;

$client->setObjectMask($objectMask);
$response = $client->getBillingItem();
print_r($response)
?>
```

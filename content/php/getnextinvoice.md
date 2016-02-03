---
title: "Determining your next bill"
description: "Example on how to use getNextInvoiceTotalAmount to retrieve the pre-tax total amount of an account's next invoice measured in US Dollars ($USD). The amount assumes no changes or charges occur between now and the time of billing."
date: "2016-01-29"
classes: ["SoftLayer_Account"]
tags:
    - "billing"
    - "invoice"
---


```php
<?php

require_once './vendor/autoload.php';
$apiUsername = '';
$apiKey = '';

$client = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $apiUsername, $apiKey);

try {
    $nextinvoice = $client->getNextInvoiceTotalAmount();
    print_r($nextinvoice);
}  catch (\Exception $e) {
    die('Unable to get next invoice: ' . $e->getMessage());
}
?>
```

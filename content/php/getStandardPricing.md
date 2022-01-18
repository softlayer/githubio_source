---
title: "Find standard location pricing for a package"
description: "Use an object filter to only return the Standard Location pricing for a SoftLayer package. This is a priceItemId that is standard across all SoftLayer Datacenters"
date: "2016-08-22"
classes: ["SoftLayer_Product_Package"]
tags:
    - "object_filter"
    - "pricing"
---

With the introduction to Location-based Pricing, we updated our pricing model to represent the costs in each data center more clearly. Instead of adding premiums to a base server price, we have priced servers and services in each data center with their own location-based [SoftLayer_Product_Item_Price](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Item_Price) objects via the API. The following example shows how to get the Standard priceItemId for a package regardless of the location.

```php
<?php

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');
$packageId = 194;


try {
  $client = \SoftLayer\SoapClient::getClient('SoftLayer_Product_Package', $packageId, $apiUsername, $apiKey);
  $filter = new stdClass();
  $filter->items = new stdClass();
  $filter->items->prices = new stdClass();
  $filter->items->prices->locationGroupId = new stdClass();
  $filter->items->prices->locationGroupId->operation = 'is null';
  $client->setObjectFilter($filter);

  $standardPricing = $client->getItems();
  print_r($standardPricing);
}  catch (\Exception $e) {
  die('Cannot compute. Error is: ' . $e->getMessage());
}
?>


```

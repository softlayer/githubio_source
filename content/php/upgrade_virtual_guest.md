---
title: "Upgrade virtual guest"
description: "Upgrades a virtual guest immediately."
date: "2015-02-15"
classes: ["SoftLayer_Product_Order", "SoftLayer_Product_Package"]
tags:
    - "ordering"
    - "upgrade"
    - "virtual_guest"
---

```php
<?php

/* You can use the getenv() module to pull your exported Username
and API key to keep from having to store them in your files */

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');

$client = \SoftLayer\SoapClient::getClient('SoftLayer_Product_Order', null, $apiUsername, $apiKey);

//The price of the item you want to upgrade to
$price1 = new \stdClass();
$price1->id = 1641;

//The virtual guest you want to upgrade
$guest = new \stdClass();
$guest->id = 22983449;

$priceClient = \SoftLayer\SoapClient::getClient('SoftLayer_Product_Package', 46, $apiUsername, $apiKey);
$objectMask = new \SoftLayer\Common\ObjectMask();
$objectMask->description;
$objectMask->capacity;
$objectMask->prices->id;
$objectMask->categories->id;

$priceClient->setObjectMask($objectMask);
$items = $priceClient->getObject();
//Shows you what prices are available to select from
print_r($items);

$upgrade = new \stdClass();
$upgrade->complexType = "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade";
$upgrade->prices = array($price1);
$upgrade->properties = new \stdClass();
$upgrade->properties->maintenanceWindow;
$upgrade->properties->maintenanceWindow->name = "MAINTENANCE_WINDOW";
$upgrade->properties->maintenanceWindow->value = "now";
$upgrade->virtualGuests = array($guest);
print_r($upgrade);

//change to placeOrder($upgrade) to actually make it happen
$response = $client->placeOrder($upgrade);
print_r($response);
?>
```

---
title: "PlaceOrderUpgrade.php"
description: "PlaceOrderUpgrade.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Property"
    - "SoftLayer_Product_Order"
tags:
    - "virtualguest"
---


```php
<?php
/**
 * Order an upgrade for Virtual Guest
 *
 * This script orders an upgrade for Virtual Guest, in this case we will upgrade the "ram" for a Virtual Guest, It uses
 * SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade container and SoftLayer_Product_Order::placeOrder method for it.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade/
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Product_Item_Price/
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once "C:/Php/SoftLayer/SoftLayer/SoapClient.class.php";

/**
 * Your SoftLayer API username
 * @var string
 */
$username = "set me";

/**
 * Your SoftLayer API key
 * Generate one at: https://control.softlayer.com/account/users
 * @var string
 */
$apiKey = "set me";

/**
 * Declare the id for virtual guest to place an upgrade
 * @var int
 */
$virtualId = 9477039;

// Create a SoftLayer API client object for "SoftLayer_Product_Order" services
$productService = SoftLayer_SoapClient::getClient("SoftLayer_Product_Order", null, $username, $apiKey);

/*
 * Define a collection of SoftLayer_Product_Item_Price objects. You can verify the item available for a given package using
 * SoftLayer_Product_Package::getItemPrices method
 */
$price = new stdClass();
$price -> id = 1645; // 2 GB RAM

$prices = array();
$prices[] = $price;

// Build skeleton SoftLayer_Container_Product_Order_Property object to place an upgrade
$properties = new stdClass();
$properties -> name = "MAINTENANCE_WINDOW";
$properties -> value = "2015-07-01T09:00:00+12:00";
$propertiesVsi = array();
$propertiesVsi[] = $properties;

// Build skeleton SoftLayer_Virtual_Guest object with the Virtual Guest to place an upgrade.
$virtualGuests = new stdClass();
$virtualGuests -> id = $virtualId;
$virtualGuestList = array();
$virtualGuestList[] = $virtualGuests;

/*
 * Build a skeleton SoftLayer_Container_Product_Order object with details required to place an upgrade
 */
$orderData = new stdClass();
$orderData -> containerIdentifier = "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade";
$orderData -> prices = $prices;
$orderData -> properties = $propertiesVsi;
$orderData -> virtualGuests = $virtualGuestList;

try {
    /*
     * SoftLayer_Product_Order::verifyOrder() method will check your order for errors. Replace this with a call
     * to placeOrder() when you're ready to order. Both calls return a receipt object that you can use for your
     * records.
     */
    $orderTemplate = new SoapVar($orderData, SOAP_ENC_OBJECT, 'SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade', 'http://api.service.softlayer.com/soap/v3/');
    $result = $productService -> verifyOrder($orderTemplate);
    print_r($result);
} catch(Exception $e) {
    echo "Unable to place an upgrade for Virtual Guest: " . $e -> getMessage();
}

```

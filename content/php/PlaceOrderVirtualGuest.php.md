---
title: "PlaceOrderVirtualGuest.php"
description: "PlaceOrderVirtualGuest.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Guest"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "virtualguest"
---


```php
<?php
/**
 * Order Virtual Guest
 *
 * This script orders a Virtual Guest using SoftLayer_Product_Order::placeOrder
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
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

// Create a SoftLayer API client object for "SoftLayer_Product_Order" services
$productService = SoftLayer_SoapClient::getClient("SoftLayer_Product_Order", null, $username, $apiKey);

/**
 * Define Virtual Guest's properties
 * @var int $quantity
 * @var string $location
 * @var int $packageId
 */
$quantity = 1;
$location = "SINGAPORE";
$packageId = 46;

/*
 * Build a skeleton SoftLayer_Hardware object to define hostname and domain that we wish for the Virtual Guest.
 */
$hardware = new stdClass();
$hardware -> hostname = "Test";
$hardware -> domain = "new.new.com";
$hardwareHD = array();
$hardwareHD[] = $hardware;

/*
 * Define a collection of SoftLayer_Product_Item_Price objects. You can verify the item available for a given package using
 * SoftLayer_Product_Package::getItemPrices method
 */
$prices = array(1640, // 1 x 2.0 GHz Core
    1644, // 1 GB RAM
    13940, // CentOS 6.x - LAMP Install (32 bit)
    2202, // 25 GB (SAN)
    50241, // 5000 GB Bandwidth
    273, // 100 Mbps Public & Private Network Uplinks
    2302, // Monitoring Package - Basic
    55, // Host Ping
    58, // Automated Notification
    420, // Unlimited SSL VPN Users & 1 PPTP VPN User per account
    418, // Nessus Vulnerability Assessment & Reporting
    21, // 1 IP Address
    57, // Email and Ticket
    905, // Reboot / Remote Console
    14022 // International Services
);
// SoftLayer_Product_Item_Price objects. These objects contain much more than
// ids, but SoftLayer's ordering system only needs the price's id to know what
// you want to order.
$orderPrices = array();

foreach ($prices as $priceId) {
    $price = new stdClass();
    $price -> id = $priceId;
    $orderPrices[] = $price;
}
/*
 * Build a skeleton SoftLayer_Container_Product_Order object with details required to order
 */
$orderData = new stdClass();
$orderData -> containerIdentifier = "SoftLayer_Container_Product_Order_Virtual_Guest";
$orderData -> location = $location;
$orderData -> quantity = $quantity;
$orderData -> packageId = $packageId;
$orderData -> prices = $orderPrices;
$orderData -> hardware = $hardwareHD;

try {
    /*
     * SoftLayer_Product_Order::verifyOrder() method will check your order for errors. Replace this with a call
     * to placeOrder() when you're ready to order. Both calls return a receipt object that you can use for your
     * records.
     */
    $result = $productService -> verifyOrder($orderData);
    print_r($result);
} catch(Exception $e) {
    echo "Unable to order Virtual Guest: " . $e -> getMessage();
}

```

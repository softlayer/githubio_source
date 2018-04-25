---
title: "OrderEnduranceBlockStorage.php"
description: "OrderEnduranceBlockStorage.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order_Network_Storage_Enterprise"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "networkstorage"
---


```
<?php
/**
 * Order Endurance Block Storage
 *
 * This script orders an Endurance Block Storage
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Enterprise
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once dirname(__FILE__) . "/SoftLayer/SoapClient.class.php";

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
 * Declare the location, packageId and quantity for the Endurance that you wish to order
 * @var int $location
 * @var int $packageId
 * @var int $quantity
 */
$location = 265592; // Amsterdam 1
$packageId = 240; // the packageID for order Endurance
$quantity = 1;

// Create a SoftLayer API client object for "SoftLayer_Product_Order" service
$client = SoftLayer_SoapClient::getClient('SoftLayer_Product_Order', null, $username, $apiKey);

/**
 * Build a skeleton SoftLayer_Product_Item_Price objects. These objects contain
 * much more than ids, but SoftLayer's ordering system only needs the price's id
 * to know what you want to order.
 * To get the list of valid prices for the package
 * use the SoftLayer_Product_Package:getItems method
 */
$prices = array(45058, // Endurance Storage
45098, // Block Storage
45068, // 0.25 IOPS per GB
45148 // 40 GB Storage Space
);

$orderPrices = array();
foreach ($prices as $priceId) {
    $price = new stdClass();
    $price -> id = $priceId;
    $orderPrices[] = $price;
}

// This should match the OS type of the host(s) that will connect to the volume. The only required property is the keyName.
$osFormatType = new stdClass();
$osFormatType -> id = 12;
$osFormatType -> keyName = "LINUX";
$osFormatType -> name = "Linux";

// Build a SoftLayer_Container_Product_Order_Network_Storage_Enterprise object containing
// the order you wish to place.
$orderContainer = new stdClass();
$orderContainer -> location = $location;
$orderContainer -> packageId = $packageId;
$orderContainer -> prices = $orderPrices;
$orderContainer -> quantity = $quantity;
$orderContainer -> osFormatType = $osFormatType;


// Re-declare the order template as a SOAP variable, so the SoftLayer ordering system knows what type of order you're placing.
$orderTemplate = new SoapVar($orderContainer, SOAP_ENC_OBJECT, 'SoftLayer_Container_Product_Order_Network_Storage_Enterprise', 'http://api.service.softlayer.com/soap/v3/');

try {
    /**
     * We will use verifyOrder() method to check for errors. Replace this with placeOrder() when you are ready to order.
     * @see http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
     */
    $result = $client -> placeOrder($orderTemplate);
    print_r($result);
} catch(Exception $e) {
    echo "Unable to order Endurance Block Storage" . $e -> getMessage();
}

```

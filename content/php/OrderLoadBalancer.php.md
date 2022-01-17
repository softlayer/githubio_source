---
title: "OrderLoadBalancer.php"
description: "OrderLoadBalancer.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Network_LoadBalancer"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Order"
tags:
    - "loadbalancers"
---


```php
<?php
/**
 * This script orders a Load Balancer
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once __DIR__.'/vendor/autoload.php';

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

// Define the package id that you wish to order
$packageId = 194;

// Define the location 
$location = "265592"; // Amsterdam 1

// Building a skeleton SoftLayer_Product_Item_Price object.
// The object contains the price Id of the Load Balancer that you wish to order.
$prices = array(17221);

/**
 * Convert our item list into an array of skeleton
 * SoftLayer_Product_Item_Price objects. These objects contain much more than
 * ids, but SoftLayer's ordering system only needs the price's id to know what
 * you want to order.
 */
$orderPrices = array();
 
foreach ($prices as $priceId){
    $price = new stdClass();
    $price->id = $priceId;
    $orderPrices[] = $price;
} 

// Create a SoftLayer API client object to the "SoftLayer_Product_Order" service
$orderService = \SoftLayer\SoapClient::getClient('SoftLayer_Product_Order', null, $username, $apiKey);


// Build a SoftLayer_Container_Product_Order_Network_LoadBalancer object containing
// the order you wish to place.
$orderData = new stdClass();
$orderData -> packageId = $packageId;
$orderData -> prices = $orderPrices;
$orderData -> location = $location;

try {
	/**
	 * Re-declare the order template as a SOAP variable, so the SoftLayer
	 * ordering system knows what type of order you're placing.
	 */
    $orderTemplate = new SoapVar
    (
        $orderData,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Product_Order_Network_LoadBalancer',
        'http://api.service.softlayer.com/soap/v3/'
    );
 
    /**
	 * verifyOrder() will check your order for errors. Replace this with a call
	 * to placeOrder() when you're ready to order. Both calls return a receipt
	 * object that you can use for your records.
	 * 
	 * Once your order is placed it'll go through SoftLayer's approval and
	 * provisioning process.
	 */ 
    $receipt = $orderService -> verifyOrder($orderTemplate);
    print_r($receipt);
    
} catch(Exception $e) {
    echo "Unable to order Load Balancer: " . $e -> getMessage();
}

```

---
title: "PlaceOrderCDN.php"
description: "PlaceOrderCDN.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Container_Product_Order_Monitoring_Package"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_ContentDelivery_Account"
tags:
    - "cdn"
---


```
<?php
/**
 * Order a new CDN account
 *
 * Build a SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
 * object for a new CDN account order and pass it to the SoftLayer_Product_Order
 * API service to order it. In this script we'll order a pay as you go bandwidth
 * and storage CDN account. See below for more details.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_ContentDelivery_Account
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Order/verifyOrder
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Order/placeOrder
 *
 * License: http://sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('Softlayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

// Create a SoftLayer API client object
$softLayer_product_order = SoftLayer_SoapClient::getClient('SoftLayer_Product_Order', null, $username, $key);

/**
 * Build a skeleton SoftLayer_Product_Item_Price objects. These objects contain
 * much more than ids, but SoftLayer's ordering system only needs the price's id
 * to know what you want to order.
 * to get the list of valid prices for the package
 * use the SoftLayer_Product_Package:getItems method
 */
$prices = array
(
    # Price to 10Mbps Hardware Firewall 
    1661, # CDN Pay as You Go Bandwidth
    1670 # CDN No storage (origin pull)
);

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

$packageId = 208;  // The package id to order Content Delivery Network
$quantity = 1;   


// Build a SoftLayer_Container_Product_Order_Monitoring_Package object containing
// the order you wish to place.
$orderContainer = new stdClass();
$orderContainer->packageId          = $packageId;
$orderContainer->prices             = $orderPrices;
$orderContainer->quantity           = $quantity;

// Place the order for the new server.
try {
    // Re-declare the order template as a SOAP variable, so the SoftLayer
    // ordering system knows what type of order you're placing.
    $orderTemplate = new SoapVar
    (
        $orderContainer,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Product_Order_Network_ContentDelivery_Account',
        'http://api.service.softlayer.com/soap/v3/'
    );
 
    // verifyOrder() will check your order for errors. Replace this with a call
    // to placeOrder() when you're ready to order. Both calls return a receipt
    // object that you can use for your records.
    //
    // Once your order is placed it'll go through SoftLayer's approval and
    // provisioning process. 
    $receipt = $softLayer_product_order->verifyOrder($orderTemplate);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to place the order: ' . $e->getMessage();
}

```

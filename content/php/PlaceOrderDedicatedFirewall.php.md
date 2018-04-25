---
title: "PlaceOrderDedicatedFirewall.php"
description: "PlaceOrderDedicatedFirewall.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Container_Product_Order_Monitoring_Package"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "firewall"
---


```
<?php
/**
 * Order dedicated Firewall

 * Important manual pages:
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
 * 
 * License <http://sldn.softlayer.com/wiki/index.php/license>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
require_once ('Softlayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

// Creating a SoftLayer API client object
$softLayerProductOrder = SoftLayer_SoapClient::getClient('SoftLayer_Product_Order', null, $username, $key);

/**
 * Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
 * much more than ids, but SoftLayer's ordering system only needs the price's id
 * to know what you want to order.
 * to get the list of valid prices for the package
 * use the SoftLayer_Product_Package:getItems method
*/
$prices = array
(
    410, # Price to 10Mbps Hardware Firewall
);

/**
 * Convert our item list into an array of skeleton
 * SoftLayer_Product_Item_Price objects. 
 */
$orderPrices = array();
 
foreach ($prices as $priceId){
    $price = new stdClass();
    $price->id = $priceId;
    $orderPrices[] = $price;
}

$location = "AMSTERDAM";
$packageId = 0;  // The package Id for order monitoring packages is 0
$quantity = 1;   

// Build a skeleton SoftLayer_Virtual_Guest object to model the id
// of the virtual guest where you want add the monitoring package
$virtualGuests = new stdClass();
$virtualGuests->id = 6674100;
$orderVirtualGuest = array
(
    $virtualGuests
);

// Build a SoftLayer_Container_Product_Order_Monitoring_Package object containing
// the order you wish to place.
$orderContainer = new stdClass();
$orderContainer->location           = $location;
$orderContainer->packageId          = $packageId;
$orderContainer->prices             = $orderPrices;
$orderContainer->quantity           = $quantity;
$orderContainer->virtualGuests      = $orderVirtualGuest;

// Place the order for the new server.
try {
    // Re-declare the order template as a SOAP variable, so the SoftLayer
    // ordering system knows what type of order you're placing.
    $orderTemplate = new SoapVar
    (
        $orderContainer,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Product_Order_Network_Protection_Firewall',
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
    $receipt = $softLayerProductOrder->verifyOrder($orderTemplate);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to place server order: ' . $e->getMessage();
}

```

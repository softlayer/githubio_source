---
title: "PlaceOrderVlan.php"
description: "PlaceOrderVlan.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order_Monitoring_Package"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Container_Product_Order_Network_Vlan"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "vlan"
---


```php
<?php
/**
 * Example to create a new VLAN.
 * 
 * The script uses the placeOrder method to order
 * a new VLAN with 32 static IP address
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Vlan
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
 * 
 * License: http://sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('Softlayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

# Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
# much more than ids, but SoftLayer's ordering system only needs the price's id
# to know what you want to order.
# to get the list of valid prices for the package
# use the SoftLayer_Product_Package:getItems method
$prices = array
(
    # The price for the new Public Network Vlan
    2018,
    # The price for 32 Static Public IP Addresses
    36716
);

// Converting our item list into an array of skeleton
// SoftLayer_Product_Item_Price objects. These objects contain much more than
// ids, but SoftLayer's ordering system only needs the price's id to know what
// you want to order.
$orderPrices = array();
 
foreach ($prices as $priceId){
    $price = new stdClass();
    $price->id = $priceId;
    $orderPrices[] = $price;
}

$location = "AMSTERDAM";
$packageId = 0;  // The packageID for order monitoring packages is 0
$quantity = 1;   
$sendQuoteEmailFlag = true;
$name = "myNewVlan";
# The router ID where the VLAN will be created
# to get the list of routers in your account
# use the SoftLayer_Account::getRouters method
$routerId = 117960; 

// Building a SoftLayer_Container_Product_Order_Monitoring_Package object containing
// the order you wish to place.
$orderContainer = new stdClass();
$orderContainer->location           = $location;
$orderContainer->packageId          = $packageId;
$orderContainer->prices             = $orderPrices;
$orderContainer->quantity           = $quantity;
$orderContainer->sendQuoteEmailFlag = $sendQuoteEmailFlag;
$orderContainer->name = $name;
$orderContainer->routerId = 117960;

// Creating a SoftLayer API client object
$softLayerProductOrder = SoftLayer_SoapClient::getClient('SoftLayer_Product_Order', null, $username, $key);

// Placing the order for the new server.
try {
    // Re-declare the order template as a SOAP variable, so the SoftLayer
    // ordering system knows what type of order you're placing.
    $orderTemplate = new SoapVar
    (
        $orderContainer,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Product_Order_Network_Vlan',
        'http://api.service.softlayer.com/soap/v3/'
    );
 
    // verifyOrder() will check your order for errors. Replace this with a call
    // to placeOrder() when you're ready to order. Both calls return a receipt
    // object that you can use for your records.
    //
    // Once your order is placed it'll go through SoftLayer's approval and
    // provisioning process. 
    $receipt = $softLayerProductOrder->verifyOrder($orderTemplate);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to place order: ' . $e->getMessage();
}

```

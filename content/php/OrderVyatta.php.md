---
title: "OrderVyatta.php"
description: "OrderVyatta.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance"
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Hardware_Server"
tags:
    - "viyatta"
---


```
<?php
/**
 * Order a Network Gateway Appliance (Vyatta)
 * 
 * The script orders a (Vyatta) high availability pair
 * it uses the SoftLayer_Product_Order::placeOrder to make the order
 * For more information see below:
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
 * 
 * License: http://sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('Softlayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

/**
 * Build a skeleton SoftLayer_Hardware_Server object to model the hostname and
 * domain we want for our server. If you set quantity greater than 1 then you
 * need to define one hostname/domain pair per server you wish to order. 
 */
$hardwareNode1 = new stdClass();
$hardwareNode1->hostname = "vyattagw";
$hardwareNode1->domain = "test.com";
$hardwareNode2 = new stdClass();
$hardwareNode2->hostname = "vyattagw2";
$hardwareNode2->domain = "test.com";
$orderHardware = array
(
    $hardwareNode1,$hardwareNode2
);

/**
 * Build a skeleton SoftLayer_Product_Item_Price objects. These objects contain
 * much more than ids, but SoftLayer's ordering system only needs the price's id
 * to know what you want to order.
 *
 * Every item in SoftLayer's product catalog is assigned an id. Use these ids
 * to tell the SoftLayer API which options you want in your new server. Use
 * the getActivePackages() method in the SoftLayer_Account API service to get
 * a list of available item and price options per available package.
 */
$prices = array
(
    13738,  
    21010,  
    36044,  
    876,  
    1267, 
    342,  
    273, 
    17129,
    55,  
    58,  
    420, 
    418, 
    21,  
    57,  
    906,
);

/**
 * Converting our item list into an array of skeleton
 * SoftLayer_Product_Item_Price objects. These objects contain much more than
 * ids, but SoftLayer's ordering system only needs the price's id to know what
 * you want to order.
 * 
 */
$orderPrices = array();
 
foreach ($prices as $priceId){
    $price = new stdClass();
    $price->id = $priceId;
    $orderPrices[] = $price;
}

/**
 * Where you'd like your new server provisioned.
 * This can either be the id of the datacenter
 * you wish your new server to be provisioned in
 * 
 */
$location = 265592;
// The id of the SoftLayer_Product_Package you wish to order.
// In this case the Network Gateway Appliance (Vyatta) package id is 174.
$packageId = 174;
// The number of servers you wish to order.
// If you wish a high availability pair you must specify 2 as quantity.
$quantity = 2;
// Build a SoftLayer_Container_Product_Order object containing
// the order you wish to place.
$orderContainer = new stdClass();
$orderContainer->location    = $location;
$orderContainer->packageId   = $packageId;
$orderContainer->prices      = $orderPrices;
$orderContainer->quantity    = $quantity;
$orderContainer->hardware    = $orderHardware;

$orderContainers = array();
$orderContainers[0] = $orderContainer;

$orderData = new stdClass();
$orderData->orderContainers = $orderContainers;


// Create a SoftLayer API client object
$softLayerProductOrder = SoftLayer_SoapClient::getClient('SoftLayer_Product_Order', null, $username, $key);

// Place the order for the new server.
try {
    // Re-declare the order template as a SOAP variable, so the SoftLayer
    // ordering system knows what type of order you're placing.
    $orderTemplate = new SoapVar
    (
        $orderData,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Product_Order',
        'http://api.service.softlayer.com/soap/v3/'
    );
  
    /**
     * verifyOrder() will check your order for errors. Replace this with a call
     * to placeOrder() when you're ready to order. Both calls return a receipt
     * object that you can use for your records.
     *
     * Once your order is placed it'll go through SoftLayer's approval and
     * provisioning process. When it's done you'll have a new
     * SoftLayer_Hardware_Server object and server ready to use.
     * 
     */
    $receipt = $softLayerProductOrder->verifyOrder($orderTemplate);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to place server order: ' . $e->getMessage();
}

```

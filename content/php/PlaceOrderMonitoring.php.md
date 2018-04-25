---
title: "PlaceOrderMonitoring.php"
description: "PlaceOrderMonitoring.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order_Monitoring_Package"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Order"
tags:
    - "monitoring"
---


```
<?php
/**
 * Example to order a portal monitoring
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Monitoring_Package
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
 * 
 * License <http://sldn.softlayer.com/article/License>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 *
*/
require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

# Every item in SoftLayer's product catalog is assigned an id. Use these ids
# to tell the SoftLayer API which options you want in your new server. Use
# the getActivePackages() method in the SoftLayer_Account API service to get
# a list of available item and price options per available package.
$prices = array
(
    # This is the price for Monitoring Package - Basic ((Hardware and OS))
    2302,
);

# Converting our item list into an array of skeleton
# SoftLayer_Product_Item_Price objects. These objects contain much more than
# ids, but SoftLayer's ordering system only needs the price's id to know what
# you want to order.
$orderPrices = array();
 
foreach ($prices as $priceId){
    $price = new stdClass();
    $price->id = $priceId;
    $orderPrices[] = $price;
}

$location = "SANJOSE";
$packageId = 0;  # The packageId for order monitoring packages is 0
$quantity = 0;   # The quantity for order a service (in this case monitoring package) must be 0
$sendQuoteEmailFlag = true;
$useHourlyPricing = true;


# Building a skeleton SoftLayer_Virtual_Guest object to model the Id
# of the virtual guest where you want add the monitoring package
$virtualGuests = new stdClass();
$virtualGuests->id = 4906034;
$orderVirtualGuest = array
(
    $virtualGuests
);

$configurationTemplateGroups = new stdClass();
$configurationTemplateGroups->id = 3; # The templateId for the monitoring group (in this case Basic Monitoring package for Unix/Linux operating system.)  
$orderConfigurationTemplateGroups = array
(
    $configurationTemplateGroups
);



# Build a SoftLayer_Container_Product_Order_Monitoring_Package object containing
# the order you wish to place.
$orderContainer = new stdClass();
$orderContainer->location           = $location;
$orderContainer->packageId          = $packageId;
$orderContainer->prices             = $orderPrices;
$orderContainer->quantity           = $quantity;
$orderContainer->sendQuoteEmailFlag = $sendQuoteEmailFlag;
$orderContainer->useHourlyPricing   = $useHourlyPricing;
$orderContainer->virtualGuests      = $orderVirtualGuest;
$orderContainer->configurationTemplateGroups      = $orderConfigurationTemplateGroups;

# Create a SoftLayer API client object
$softLayer_product_order = SoftLayer_SoapClient::getClient('SoftLayer_Product_Order', null, $username, $key);

# Place the order for the new server.
try {
    # Re-declare the order template as a SOAP variable, so the SoftLayer
    # ordering system knows what type of order you're placing.
    $orderTemplate = new SoapVar
    (
        $orderContainer,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Product_Order_Monitoring_Package',
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
     */
    $receipt = $softLayer_product_order->verifyOrder($orderTemplate);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to place monitoring order: ' . $e->getMessage();
}

?>

```

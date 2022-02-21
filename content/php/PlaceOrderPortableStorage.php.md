---
title: "PlaceOrderPortableStorage.php"
description: "PlaceOrderPortableStorage.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Container_Product_Order_Virtual_Disk_Image"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "portablestorage"
---


```php
<?php
/**
 * Example to order a portal storage
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Disk_Image
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
 * 
 * License: http:'sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('Softlayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

/**
 * Every item in SoftLayer's product catalog is assigned an id. Use these ids
 * to tell the SoftLayer API which options you want in your new server. Use
 * the getActivePackages() method in the SoftLayer_Account API service to get
 * a list of available item and price options per available package.
 * 
 */
$prices = array
(
    /**    
     * The prices for the portable storage
     * to see the list of prices available for the package
     * use the Softlayer_Product_Package::getItems method (http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems)
     * e.g.
     * client = SoftLayer::Client.new(:username => user,:api_key => api_key)
     * productPackageService = client.service_named("Softlayer_Product_Package")
     * packageID = 198
     * result = productPackageService.object_with_id(packageID).getItems() 
     */
    21861,
);

/**
 * Convert our item list into an array of skeleton
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

$location = "SANJOSE";
$packageId = 198;
$diskDescription = "test portable storage";

/**
 * Build a SoftLayer_Container_Product_Order_Virtual_Disk_Image object containing
 * the order you wish to place. 
 */
$orderContainer = new stdClass();
$orderContainer->location           = $location;
$orderContainer->packageId          = $packageId;
$orderContainer->prices             = $orderPrices;
$orderContainer->diskDescription    = $diskDescription;

// Create a SoftLayer API client object
$softLayerProductOrder = SoftLayer_SoapClient::getClient('SoftLayer_Product_Order', null, $username, $key);

// Place the order for the new server.
try {
    /**
     * Re-declare the order template as a SOAP variable, so the SoftLayer
     * ordering system knows what type of order you're placing. 
     */
    $orderTemplate = new SoapVar
    (
        $orderContainer,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Product_Order_Virtual_Disk_Image',
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
    $receipt = $softLayerProductOrder->verifyOrder($orderTemplate);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to place the order: ' . $e->getMessage();
}

```

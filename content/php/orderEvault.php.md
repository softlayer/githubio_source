---
title: "orderEvault.php"
description: "orderEvault.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault"
    - "SoftLayer_Product_Order"
tags:
    - "evault"
---


```php
<?php
# Example to order a Evault
# reference pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require_once ('Softlayer/SoapClient.class.php');

// Your SoftLayer API username and key.
// Generate an API key at the SoftLayer Customer Portal:
// https://manage.softlayer.com/Administrative/apiKeychain
$username = 'set me';
$key = 'set me';

// Create a SoftLayer API client object
$softLayer_product_order = SoftLayer_SoapClient::getClient('SoftLayer_Product_Order', null, $username, $key);

# Build a skeleton SoftLayer_Hardware object.
# The object contains the hardware ID of the
# Bare Metal server wich will contain the Evault
# If you want use a Virtual Server instead a
# Bare Metal server build a skeleton SoftLayer_Virtual_Guest object
$virtualGuests = new stdClass();
$virtualGuests->id = 4241550;
$orderVirtualGuest = array
(
    $virtualGuests,
);

# The location for the Evault
$location = "DALLAS06";
$packageId = 0;
$quantity = 1;

// Build a skeleton SoftLayer_Product_Item_Price object.
// The object contains the price ID of the Evaul device
// you wish order.
$prices = array
(
    1045,
);

// Convert our item list into an array of skeleton
// SoftLayer_Product_Item_Price objects. These objects contain much more than
// ids, but SoftLayer's ordering system only needs the price's id to know what
// you want to order.
$orderPrices = array();
 
foreach ($prices as $priceId){
    $price = new stdClass();
    $price->id = $priceId;
    $orderPrices[] = $price;
}

// Build a SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault object containing
// the order you wish to place.
$orderTemplate = new stdClass();
$orderTemplate->location         = $location;
$orderTemplate->packageId        = $packageId;
$orderTemplate->prices           = $orderPrices;
$orderTemplate->quantity         = $quantity;
$orderTemplate->virtualGuests    = $orderVirtualGuest;

print_r($orderTemplate);

// Place the order.
try {
    // Re-declare the order template as a SOAP variable, so the SoftLayer
    // ordering system knows what type of order you're placing.
    $orderTemplate = new SoapVar
    (
        $orderTemplate,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault',
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
    echo 'Unable to place server order: ' . $e->getMessage();
}

?>
```

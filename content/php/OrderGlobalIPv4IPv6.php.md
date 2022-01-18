---
title: "OrderGlobalIPv4IPv6.php"
description: "OrderGlobalIPv4IPv6.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Container_Product_Order_Network_Subnet"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
tags:
    - "subnet"
---


```php
<?php
/**
 * Order a new Global IPv4/IPv6 subnet
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Subnet
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 */
$apiUsername = 'set me';
$apiKey = 'set me';

/**
 * Set the service to use
 */
$serviceName ='SoftLayer_Product_Order';

/**
 * The number of subnets you want to order
 *
 * @var int;
 */
$quantity = 1;

$packageId = 0;
$packageService ='SoftLayer_Product_Package';
$orderService ='SoftLayer_Product_Order';

/**
 * Create a client to the API services to use.
 */
$packageClient = SoftLayer_SoapClient::getClient($packageService, $packageId, $apiUsername, $apiKey);
$orderClient = SoftLayer_SoapClient::getClient($orderService, null, $apiUsername, $apiKey);

/**
 * Declaring an object filter to get specific subnet type to order e.g. GLOBAL_IPV6, GLOBAL_IPV4
 */
$filter = new stdClass();
$filter->itemPrices = new stdClass();
$filter->itemPrices->item = new stdClass();
$filter->itemPrices->item->keyName = new stdClass();
$filter->itemPrices->item->keyName->operation = new stdClass();
$filter->itemPrices->item->keyName->operation = "GLOBAL_IPV6";

try {

    $packageClient->setObjectFilter($filter);
    $packageResult = $packageClient->getItemPrices();
    print_r($packageResult);

    /**
     * Get the price ID
     */
    $priceId = $packageResult[0]->id;

    $orderTemplate = new stdClass();
    $orderTemplate->packageId           = $packageId;
    $orderTemplate->prices              = array();
    $orderTemplate->prices[0]           = new stdClass();
    $orderTemplate->prices[0]->id       = $priceId;
    $orderTemplate->quantity            = $quantity;

    // Create a SoftLayer API client object to the SoftLayer_Product_Order service.
    $orderClient = SoftLayer_SoapClient::getClient
        (
            'SoftLayer_Product_Order',
            null,
            $apiUsername,
            $apiKey
        );

    /**
     * Place the order for the new subnet.
     */
    try {
        /**
         * Re-declare the order template as a SOAP variable, so the SoftLayer
         * ordering system knows what type of order you're placing.
         */
        $orderTemplate = new SoapVar
        (
            $orderTemplate,
            SOAP_ENC_OBJECT,
            'SoftLayer_Container_Product_Order_Network_Subnet',
            'http://api.service.softlayer.com/soap/v3/'
        );

        $receipt = $orderClient->verifyOrder($orderTemplate);
        print_r($receipt);
    } catch (Exception $e) {
        echo 'Unable to place subnet order: ' . $e->getMessage();
    }

} catch (Exception $e) {
    echo 'Failed ... Unable to get the item prices: ' . $e->getMessage();
}

```

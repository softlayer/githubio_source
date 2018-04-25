---
title: "OrderPortablePublicIPv6.php"
description: "OrderPortablePublicIPv6.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Container_Product_Order_Network_Subnet"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Product_Order"
tags:
    - "subnet"
---


```
<?php
/**
 * Order a new Portable Public IPv6.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Subnet
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

$priceId =  1482;  // Public Portable IPv6 Addresses

/**
 * Set a VLAN to establish where the new IP addresses are routed
 *
 * @var int
 */
$endPointVlanId = 527900;

/**
 * The number of subnets you want to order
 *
 * @var int;
 */
$quantity = 1;

/**
 * Build a SoftLayer_Container_Product_Order_Network_Subnet object containing
 * the order you want to place. Subnet's don't have a package, so set packageId
 * to 0. Since this order is for one item with no sub-options you only have to
 * set a single price id in this order.
 */
$orderTemplate = new stdClass();
$orderTemplate->packageId           = 0;
$orderTemplate->prices              = array();
$orderTemplate->prices[0]           = new stdClass();
$orderTemplate->prices[0]->id       = $priceId;
$orderTemplate->endPointVlanId      = $endPointVlanId;
$orderTemplate->quantity            = $quantity;

/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, null, $apiUsername, $apiKey);

/**
 * Create a SoftLayer API client object to the SoftLayer_Product_Order service.
 */
$client = SoftLayer_SoapClient::getClient
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

    /**
     * verifyOrder() will check your order for errors. Replace this with a call
     * to placeOrder() when you're ready to order. Both calls return a receipt
     * object that you can use for your records.
     *
     * Once your order is placed it'll go through SoftLayer's approval and
     * provisioning process. When it's done you'll have a new
     * SoftLayer_Network_Subnet object ready to use.
     */
    $receipt = $client->verifyOrder($orderTemplate);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to place subnet order: ' . $e->getMessage();
}

```

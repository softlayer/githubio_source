---
title: "Upgrade.php"
description: "Upgrade.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade"
tags:
    - "virtualguest"
---


```php
<?php
/**
 * Upgrade a Virtual Server.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 * */
$apiUsername = 'set me';
$apiKey = 'set me';

/**
 * Set the service to use.
 */
$serviceName ='SoftLayer_Product_Order';

/**
 * Set the server id that you want to upgrade.
 */
$serverId = 10403817;

/**
 * Set the new RAM value
 * e.g.: id: 1645 ==> 2 GB RAM
 */
$newRamValue = 1645;

/**
 * Set the new CPU value
 * e.g.: id: 1640  ==>  1 x 2.0 GHz Core
 */
$newCpuValue = 1640;


$json = '
    {
      "prices": [
        {
          "id": '.$newRamValue.'
        },
        {
          "id": '.$newCpuValue.'
        }
      ],

      "properties": [
        {
          "name": "MAINTENANCE_WINDOW",
          "value": "now"
        }
      ],
      "virtualGuests": [
        {
          "id": '.$serverId.'
        }
      ]
    }

  ';

$upgradeTemplate = new stdClass();
$upgradeTemplate = json_decode($json,true);

/**
 * Create a client to API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, null , $apiUsername, $apiKey);

try {
     /**
     * Re-declare the order template as a SOAP variable, so the SoftLayer
     * ordering system knows what type of order you're placing.
     */
    $upgradeTemplate = new SoapVar
    (
        $upgradeTemplate,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade',
        'http://api.service.softlayer.com/soap/v3/'
    );

    /**
     * verifyOrder() will check your order for errors. Replace this with a call
     * to placeOrder() when you're ready to order. Both calls return a receipt
     * object that you can use for your records.
	 *
     * Once your order is placed it'll go through SoftLayer's approval and
     * provisioning process. When it's done you'll have a new
     * item object ready to use.
     */
    $receipt = $client->verifyOrder($upgradeTemplate);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to upgrade virtual Server instance: ' . $e->getMessage();
}

```

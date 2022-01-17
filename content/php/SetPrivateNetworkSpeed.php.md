---
title: "SetPrivateNetworkSpeed.php"
description: "SetPrivateNetworkSpeed.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_SoapClient"
tags:
    - "virtualguest"
---


```php
<?php
/**
 * Set Private Network Interface Speed.
 * It sets the private network interface speed to the new speed.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setPrivateNetworkInterfaceSpeed
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
$serviceName ='SoftLayer_Virtual_Guest';


/**
 * Set the server id that you want to change the port speed value.
 * E.g. id = 1234.
 */
$serverId = 7991612;
/**
 * Set the new value for the port speed.
 * E.g. id = 10, 100.
 */

$newPortValue = 10;

/**
 * Create a client to the SoftLayer_Virtual_Guest API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, $serverId , $apiUsername, $apiKey);

try {

    $receipt = $client->setPrivateNetworkInterfaceSpeed($newPortValue);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to change the private port speed value: ' . $e->getMessage();
}

```

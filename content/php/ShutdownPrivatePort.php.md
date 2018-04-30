---
title: "ShutdownPrivatePort.php"
description: "ShutdownPrivatePort.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_SoapClient"
tags:
    - "virtualguest"
---


```
<?php
/**
 * Shutdown Private Port.
 * It shuts down the private network port.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/shutdownPrivatePort
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
$serviceName ='SoftLayer_Virtual_Guest';

/**
 * Set the server id to shutdown the private port.
 */
$serverId = 9914387;

/**
 * Create a client to the SoftLayer_Virtual_Guest API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, $serverId, $apiUsername, $apiKey);

/**
 * Call the shutdownPrivatePort() method from SoftLayer_Virtual_Guest.
 * The expected result after executing the script is 1 (true).
 */
try {
    $result = $client->shutdownPrivatePort();
    print_r($result);

} catch(Exception $e) {
    echo "Unable to shutdown the port: " . $e -> getMessage();
}

```

---
title: "ActivePrivatePort.php"
description: "ActivePrivatePort.php"
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
 * Activate Private Port.
 * It actives the private network port.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/activatePrivatePort
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
 * Set the service to use.
 */
$serviceName ='SoftLayer_Virtual_Guest';

/**
 * Set the server id to active the private port.
 */
$serverId = 9914387;

/**
 * Create a client to the SoftLayer_Virtual_Guest API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, $serverId, $apiUsername, $apiKey);

/**
 * Call the activatePrivatePort() method from SoftLayer_Virtual_Guest.
 * The expected result after executing the script is 1 (true).
 */
try {
    $result = $client->activatePrivatePort();
    print_r($result);

} catch(Exception $e) {
    echo "Unable to activate the port: " . $e -> getMessage();
}

```

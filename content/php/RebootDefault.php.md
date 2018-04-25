---
title: "RebootDefault.php"
description: "RebootDefault.php"
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
 * Reboot Virtual Guest.
 * Power cycle a virtual guest.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/rebootDefault
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

/***
 * Set the service to use.
 */
$serviceName ='SoftLayer_Virtual_Guest';

/**
 * Set the server id that you wish to reboot.
 */
$serverId = 7991612;

/**
 * Create a client to the SoftLayer_Virtual_Guest API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, $serverId, $apiUsername, $apiKey);

/**
 * Call the rebootDefault() method from SoftLayer_Virtual_Guest.
 * The expected result after executing the script is 1 (true).
 */
try {
    /**
     * Rebooting the Virtual Guest.
     */
    $result = $client->rebootDefault();
    print_r($result);

} catch(Exception $e) {
    echo "Unable to reboot the server: " . $e -> getMessage();
}

```

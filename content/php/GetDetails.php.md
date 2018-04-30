---
title: "GetDetails.php"
description: "GetDetails.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
    - "SoftLayer_ObjectMask"
tags:
    - "virtualguest"
---


```
<?php
/**
 * Get Virtual Guest details. 
 * It retrieves virtual guest information.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

// Your SoftLayer API username.
$apiUsername = 'set me';

// Your SoftLayer API key.
$apiKey = 'set me';

// Set the SoftLayer service to use.
$serviceName ='SoftLayer_Virtual_Guest';

$serverId = 5464742;

// Create a client to the SoftLayer_Account API service.
$client = SoftLayer_SoapClient::getClient($serviceName, $serverId, $apiUsername, $apiKey);

/**
 * Create an object Mask to retrieve items related to virtual Guest.
 *
 * i.e. Operating system, operating system passwords, all network components,
 * the datacenter the server is located in
 */
$objectMask = new SoftLayer_ObjectMask();
$objectMask->operatingSystem->passwords;
$objectMask->networkComponents;
$objectMask->datacenter;

$client->setObjectMask($objectMask);

try {
    $getDetails = $client->getObject();
    print_r($getDetails);
} catch(Exception $e) {
    echo "Unable to get Virtual Guest's details: " . $e -> getMessage();
}

```

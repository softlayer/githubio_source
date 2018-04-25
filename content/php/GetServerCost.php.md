---
title: "GetServerCost.php"
description: "GetServerCost.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_ObjectMask"
tags:
    - "billing"
---


```
<?php
/**
 * Get the recurring cost of a single server or all servers on your account.
 *
 * Get a list of servers on a SoftLayer account along with their recurring
 * monthly costs. We can get that by calling getHardware() in the
 * SoftLayer_Account API service with an object mask to retrieve cost.
 *
 * Important manual pages
 * http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
 * http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getCost
 * License: http:'sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('C:/scripst/getdetails/SoftLayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

/**
 * Method one: Getting the cost for every server on your account.
 *
 * Create a connection to the SoftLayer_Account API service and call the
 * getHardware() method to get a list of hardware on our account. Put an object
 * mask in the API call to retrieve the cost associated with hardware to get
 * every server's cost along with our hardware records.
 */
$client = Softlayer_SoapClient::getClient('SoftLayer_Account', null, $apiUsername, $apiKey);

// Adding the object mask to the call.
$objectMask = new SoftLayer_ObjectMask();
$objectMask->hardware->cost;
$client->setObjectMask($objectMask);

try {
    // Retrieving our account's hardware records.
    $hardware = $client->getHardware();
    print_r($hardware);
} catch (Exception $e) {
    die('Unable to retrieve hardware list: ' . $e->getMessage());
}

?>

```

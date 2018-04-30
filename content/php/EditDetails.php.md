---
title: "EditDetails.php"
description: "EditDetails.php"
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
 * Edit details of a Virtual Guest.
 * It edits a computing instance's properties
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/editObject
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

// Set your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

// Set the service to use
$serviceName ='SoftLayer_Virtual_Guest';

// Set the server id that you want to edit.
$serverId = 5464742;

// Create a client to the SoftLayer_Virtual_Guest API service.
$client = SoftLayer_SoapClient::getClient($serviceName, $serverId, $apiUsername, $apiKey);

/**
 * Create an object template with data that you want to edit.
 * For example: I want to edit the "hostname" and "notes".
 */
$templateObject = new stdClass();
$templateObject->hostname = 'myhostnameEdited';
$templateObject->notes = 'edited from api php';

/**
 * Call the editObject method from SoftLayer_Virtual_Guest.
 * The expected result after executing the script is 1 (true).
 */

try {
    $result = $client->editObject($templateObject);
    print_r($result);

} catch(Exception $e) {
    echo "Unable to edit the Virtual Guest's properties: " . $e -> getMessage();
}

```

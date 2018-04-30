---
title: "GetHardwareList.php"
description: "GetHardwareList.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Search"
    - "SoftLayer_Hardware"
tags:
    - "search"
---


```
<?php
/**
 * Get Hardware List From Portal>Device List.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Search/advancedSearch
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('C:\softlayer-api-php-client-master\src\SoapClient.php');

/**
 * Set your SoftLayer API username and key.
 */
$apiUsername = 'set me';
$apiKey = 'set me';

$endpointUrl = 'https://api.softlayer.com/soap/v3.1/';
$serviceName = 'SoftLayer_Search';


/**
 * Create a client to the API service.
 */
$client = \SoftLayer\SoapClient::getClient($serviceName, null, $apiUsername, $apiKey, $endpointUrl);

/**
 * The items with the following Device types should be displayed
 * using the below filter:
 *    Bar Metal Server
 */
$filterData = 'networkGatewayMemberFlag:0 _objectType:SoftLayer_Hardware';

try {
    $receipt = $client->advancedSearch($filterData);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to get the item list: ' . $e->getMessage();
}

```

---
title: "GetFirewallList.php"
description: "GetFirewallList.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Search"
    - "SoftLayer_Network_Vlan_Firewall"
tags:
    - "search"
---


```
<?php
/**
 * Get Firewall list the same as "Device List " in portal
 * using SoftLayer_Search::advancedSearch
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
 *    Firewall
 */
$filterData = '_objectType:SoftLayer_Network_Vlan_Firewall';

try {
    $receipt = $client->advancedSearch($filterData);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to get the Firewall list: ' . $e->getMessage();
}

```

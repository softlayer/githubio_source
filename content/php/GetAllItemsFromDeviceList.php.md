---
title: "GetAllItemsFromDeviceList.php"
description: "GetAllItemsFromDeviceList.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Search"
    - "SoftLayer_Hardware"
    - "SoftLayer_Network_Vlan_Firewall"
tags:
    - "search"
---


```
<?php
/**
 * Get all items from Device list.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Search/advancedSearch
 * https://sldn.softlayer.com/article/Python

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
 *    Bare Metal Server, Virtual Server, Firewall, Gateway Member, Netscaler,KVM/IP
 */
$filterData = '_objectType:SoftLayer_Hardware,'.
                'SoftLayer_Virtual_Guest,SoftLayer_Network_Vlan_Firewall,'.
                'SoftLayer_Network_Application_Delivery_Controller '.
                '_sort:[fullyQualifiedDomainName:asc]';

try {
    $receipt = $client->advancedSearch($filterData);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to get the item list: ' . $e->getMessage();
}

```

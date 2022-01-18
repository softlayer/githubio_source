---
title: "GetDevicesFilteredByPublicIP.php"
description: "GetDevicesFilteredByPublicIP.php"
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


```php
<?php
/**
 * Get Items from Device list filtered by Public IP
 * using SoftLayer_Search::advancedSearch.
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
 * Set the Public IP to filter the item list.
 */
$primaryIpAddress = '119.81.141.164';

/**
 * Create a client to the API service.
 */
$client = \SoftLayer\SoapClient::getClient($serviceName, null, $apiUsername, $apiKey, $endpointUrl);

/**
 * The items with the following Device types should be displayed
 * using the below filter:
 *    Bar Metal Server, Virtual Server, Firewall, Gateway Member, Netscaler,KVM/IP
 */
$filterData = 'primaryIpAddress: '.$primaryIpAddress .
    ' _objectType:SoftLayer_Hardware,'.
    'SoftLayer_Virtual_Guest,'.
    'SoftLayer_Network_Vlan_Firewall,'.
    'SoftLayer_Network_Application_Delivery_Controller '.
    '_sort:[fullyQualifiedDomainName:asc]';

try {
    $receipt = $client->advancedSearch($filterData);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to get the item list when filtering by primary IP Address: ' . $e->getMessage();
}

```

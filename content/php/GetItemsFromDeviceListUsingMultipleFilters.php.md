---
title: "GetItemsFromDeviceListUsingMultipleFilters.php"
description: "GetItemsFromDeviceListUsingMultipleFilters.php"
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
 * Get Gateways using SoftLayer_Search service with multiple filters
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
$apiUsername = 'set me ';
$apiKey = 'set me ';

$endpointUrl = 'https://api.softlayer.com/soap/v3.1/';
$serviceName = 'SoftLayer_Search';

/**
 * Set the location to filter the item list.
 */
$location = 'Dallas 6';

/**
 * Set the Private IP to filter the item list.
 */
$privateIpAddress = '10.107.141.195';

/**
 * Set the Device Name to filter the item list.
 */
$deviceName = 'ccnewtork3306vddal06.softlayer.local';

/**
 * Create a client to the API service.
 */
$client = \SoftLayer\SoapClient::getClient($serviceName, null, $apiUsername, $apiKey, $endpointUrl);

/**
 * The items with the following Device types should be displayed
 * using the below filter:
 *    Firewall
 */
$filterData = 'networkGatewayMemberFlag:"1" '.
                '& datacenter.longName:"'.$location .'"'.
                '& primaryBackendIpAddress:'.$privateIpAddress.
                '& fullyQualifiedDomainName:'. $deviceName.
                '_objectType:SoftLayer_Hardware';

try {
    $receipt = $client->advancedSearch($filterData);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to get the Gateways according to set of filters: ' . $e->getMessage();
}

```

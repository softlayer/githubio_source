---
title: "RouteGlobalIP.php"
description: "RouteGlobalIP.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Network_Subnet_IpAddress_Global"
    - "SoftLayer_Network_Subnet"
tags:
    - "subnet"
---


```php
<?php
/**
 * Route Global IP.
 * This function is used to create a new transaction to modify a global IP route.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet/getGlobalIpRecord
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet_IpAddress_Global/route
 *
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
 * Set the service to use
 */
$subnetService ='SoftLayer_Network_Subnet';
$subnetIpAddressGlobalService = 'SoftLayer_Network_Subnet_IpAddress_Global';

$subnetId = 880579;
$newEndPointIpAddress = '50.97.102.211';

/**
 * Create a client to the API service.
 */
$subnetClient = SoftLayer_SoapClient::getClient($subnetService, $subnetId, $apiUsername, $apiKey);

try {
    /***
     * Get the Global IP record
     */
    $globalIpRecord = $subnetClient->getGlobalIpRecord();
    $globalIpRecordId = $globalIpRecord->id;

    try{
        $subnetIpAddressGlobalClient = SoftLayer_SoapClient::getClient($subnetIpAddressGlobalService, $globalIpRecordId, $apiUsername, $apiKey);
        $result = $subnetIpAddressGlobalClient->route($newEndPointIpAddress);
        print_r($result);

    } catch(Exception $e) {
        echo 'Unable to route the global IP address: ' . $e->getMessage();
    }

} catch (Exception $e) {
    echo 'Failed ... Unable to get Global IP record: ' . $e->getMessage();
}

```

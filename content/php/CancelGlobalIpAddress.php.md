---
title: "CancelGlobalIpAddress.php"
description: "CancelGlobalIpAddress.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_ObjectMask"
tags:
    - "subnet"
---


```php
<?php
/**
 * Cancel a Global IP Address.
 * This script cancels a network subnet using its globalIpRecord billing Item.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet/getGlobalIpRecord
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
 * Set the service to use.
 */
$subnetService ='SoftLayer_Network_Subnet';
$billingItemService = 'SoftLayer_Billing_Item';

$subnetId = 880777;

/**
 * Create a client to the API service.
 */
$subnetClient = SoftLayer_SoapClient::getClient($subnetService, $subnetId, $apiUsername, $apiKey);

$mask = new SoftLayer_ObjectMask();
$mask = 'mask[id,billingItem.id]';
$subnetClient->setObjectMask($mask);

try {
    /***
     * Get the Global IP record
     */
    $globalIpRecord = $subnetClient->getGlobalIpRecord();
    $billingItemId = $globalIpRecord->billingItem->id;

    try {
        $billingItemClient = SoftLayer_SoapClient::getClient($billingItemService, $billingItemId, $apiUsername, $apiKey);
        $result = $billingItemClient->cancelItem(   False,
            False,
            'No longer needed',
            'Api test');
        print_r($result);

    } catch(Exception $e) {
        echo 'Unable to cancel the Global IP Address Subnet: ' . $e->getMessage();
    }

} catch (Exception $e) {
    echo 'Failed ... Unable to get Global IP record: ' . $e->getMessage();
}

```

---
title: "CancelSubnet.php"
description: "CancelSubnet.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Billing_Item"
tags:
    - "subnet"
---


```php
<?php
/**
 * Cancel a Subnet.
 * This script cancels a network subnet using its billing Item.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem
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
 * Set the services to use
 */
$subnetService ='SoftLayer_Network_Subnet';
$billingItemService = 'SoftLayer_Billing_Item';

$subnetId = 207873;

/**
 * Create a client to the API service.
 */
$subnetClient = SoftLayer_SoapClient::getClient($subnetService, $subnetId, $apiUsername, $apiKey);

try {
    /***
     * Get the Global IP record
     */
    $subnetResult = $subnetClient->getBillingItem();
    $billingItemId = $subnetResult->{'id'};
    print_r($billingItemId);

     try {
        $billingItemClient = SoftLayer_SoapClient::getClient($billingItemService, $billingItemId, $apiUsername, $apiKey);
        $result = $billingItemClient->cancelItem(   False,
                                                    False,
                                                    'No longer needed',
                                                    'Api test');
    print_r($result);

    } catch(Exception $e) {
    echo 'Unable to cancel the Subnet: ' . $e->getMessage();
    }


} catch (Exception $e) {
    echo 'Failed ... Unable to get billing item of Subnet: ' . $e->getMessage();
}

```

---
title: "CancelVlan.php"
description: "CancelVlan.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_ObjectMask"
tags:
    - "vlan"
---


```php
<?php
/**
 * Example to cancel a VLAN
 * 
 * The script will get the Billing_Item id of the VLAN service
 * then it will cancel the VLAN service
 * 
 * Important manual pages
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject
 * http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item
 * http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService
 * 
 * License: http://sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('SoftLayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

// The VLAN id you wish to cancel
$vlanId = 563298;

// Declaring the API client
$networkVlanService = Softlayer_SoapClient::getClient('SoftLayer_Network_Vlan', null, $apiUsername, $apiKey);
$billingItemService = Softlayer_SoapClient::getClient('SoftLayer_Billing_Item', null, $apiUsername, $apiKey);

$networkVlanService->setInitParameter($vlanId);

// Declaring an object mask to get the billing item information
$objectMask = new SoftLayer_ObjectMask();
$objectMask->billingItem;
$objectMask->billingItem->id;
$networkVlanService->setObjectMask($objectMask);

try {
    // Getting the Billing Item to cancel the VLAN service.
    $vlan = $networkVlanService->getObject();
    print_r($vlan);
    // Canceling the VLAN service.
    $billingItemService->setInitParameter($vlan->{'billingItem'}->{'id'});
    $result = $billingItemService->cancelService();
    print_r($result);
} catch (Exception $e) {
    die('Unable to cancel the VLAN. ' . $e->getMessage());
}

```

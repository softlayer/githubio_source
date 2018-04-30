---
title: "Cancel.php"
description: "Cancel.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Billing_Item"
tags:
    - "virtualguest"
---


```
<?php
/**
 * Cancel a Virtual Guest.
 * It cancels the resource for a billing Item. The billing item will be cancelled
 * immediately and reclaim of the resource will begin shortly.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject
 * http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 * */
$apiUsername = 'set me';
$apiKey = 'set me';

/**
 * Set the server id that you want to cancel.
 */
$serverId = 4905364;

/**
 * Create a client to the SoftLayer_Virtual_Guest API service.
 */
$virtualGuestService = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest', $serverId , $apiUsername, $apiKey);

try {
    /**
     * Getting the billing item id
     */
    $objectMask = 'mask[billingItem.id]';
    $virtualGuestService->setObjectMask($objectMask);
    $receipt = $virtualGuestService->getObject();
    $billingItemId = $receipt->billingItem->id;

    try {

        /**
         * Canceling the Virtual Guest
         */
        $billingItemService = SoftLayer_SoapClient::getClient('SoftLayer_Billing_Item', $billingItemId , $apiUsername, $apiKey);
        $result = $billingItemService->cancelService();
        print_r($result);

    } catch(Exception $e){

        echo 'Unable to cancel the server: ' . $e->getMessage();
    }

} catch (Exception $e) {

    echo 'Unable to get Virtual guest data: ' . $e->getMessage();
}

```

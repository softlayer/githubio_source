---
title: "GetLoadBalancers.php"
description: "GetLoadBalancers.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
tags:
    - "loadbalancers"
---


```php
<?php
/**
 * This script retrieves an account's associated load balancers.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getAdcLoadBalancers
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
 * @see http://sldn.softlayer.com/article/Object-Masks
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once __DIR__.'/vendor/autoload.php';

/**
 * Your SoftLayer API username
 * @var string
 */
$username = "set me";

/**
 * Your SoftLayer API key
 * Generate one at: https://control.softlayer.com/account/users
 * @var string
 */
$apiKey = "set me";

// Create a SoftLayer API client object to the "SoftLayer_Account" service
$accountService = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);

// Declare an object mask, to get additional information
$objectMask = "mask[ipAddress, loadBalancerHardware[datacenter]]";
$accountService -> setObjectMask($objectMask);

try {
	$loadBalancers = $accountService -> getAdcLoadBalancers();
	foreach($loadBalancers as $loadBalancer)
	{
		$notes = "";
		if(isset($loadBalancer -> notes))
		{
			$notes = $loadBalancer -> notes;
		}
		echo("VIP Address: " . $loadBalancer -> ipAddress -> ipAddress . " Device: " . $loadBalancer->loadBalancerHardware[0]->hostname . " Location: " .
                        $loadBalancer->loadBalancerHardware[0]->datacenter->longName . " SSL Offload: " . $loadBalancer -> sslEnabledFlag . " Notes: " . $notes ."\n");
	}
    
} catch(Exception $e) {
	echo "Unable to get Load Balancers: " . $e -> getMessage();
}

```

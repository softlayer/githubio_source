---
title: "GetServiceGroups.php"
description: "GetServiceGroups.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
tags:
    - "loadbalancers"
---


```
<?php
/**
 * This script retrieves service groups from a load balancer.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getAdcLoadBalancers
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/s
 * @see http://sldn.softlayer.com/article/Object-Filters
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once '\vendor\autoload.php';

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

/**
 * Define the VIP Address from load balancer that you wish to retrieve its service groups
 * @var string
 */
 $vipAddress = "159.253.157.82";

// Create a SoftLayer API client object to the "SoftLayer_Account" service
$accountervice = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);

// Declare an object filter
$filter = new stdClass();
$filter -> adcLoadBalancers = new stdClass();
$filter -> adcLoadBalancers -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress -> operation = $vipAddress;
$accountervice -> setObjectFilter($filter);

// Define an object mask, to get additional information for load balancer
$objectMask = "mask[virtualServerCount, virtualServers[serviceGroups[routingMethod, routingType]]]";
$accountervice->setObjectMask($objectMask);

try {
	// Get Load Balancer
	$loadBalancers = $accountervice -> getAdcLoadBalancers();
	
	foreach($loadBalancers[0] -> virtualServers as $virtualServer)
	{
		$notes = "";
		if(isset($virtualServer -> serviceGroups[0] -> notes ))
		{
			$notes = $virtualServer -> serviceGroups[0] -> notes ;
		}
		print_r("Group: " . $virtualServer -> serviceGroups[0] -> routingType -> name . " Method: " . $virtualServer -> serviceGroups[0] -> routingMethod -> name . 
		" Port: " . $virtualServer -> port . " Alloc: " . $virtualServer -> allocation . " Notes: " . $notes . "\n");
	}
} catch(Exception $e) {
    echo "Unable to retrieve service groups: " . $e -> getMessage();
}

```

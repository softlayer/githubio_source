---
title: "GetServicesFromServiceGroup.php"
description: "GetServicesFromServiceGroup.php"
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
 * Define the VIP Address from load balancer
 * @var string
 */
 $vipAddress = "173.193.117.96";
 
// Define the port from service group that you wish to retrieve its services
$port = 80;

// Create a SoftLayer API client object to the "SoftLayer_Account" service
$accountService = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);

// Declare an object filter
$filter = new stdClass();
$filter -> adcLoadBalancers = new stdClass();
$filter -> adcLoadBalancers -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress -> operation = $vipAddress;
$accountService -> setObjectFilter($filter);

// Define an object mask, to get additional information for load balancer
$objectMask = "mask[virtualServers[serviceGroups[services[healthChecks[type], groups, groupReferences, ipAddress]]]]";
$accountService->setObjectMask($objectMask);

try {
	// Get Load Balancer
	$loadBalancers = $accountService -> getAdcLoadBalancers();
	
	foreach($loadBalancers[0] -> virtualServers as $virtualServer)
	{
		if($virtualServer -> port == $port)
		{
			foreach($virtualServer -> serviceGroups as $serviceGroup)
			{
				foreach($serviceGroup -> services as $service)
				{
					$notes = "";
					if(isset($service -> notes))
					{
						$notes = $service -> notes;
					}
					print_r("Enabled: " . $service -> enabled . " Destination Ip: " . $service -> ipAddress -> ipAddress . " Dest. Port: ". $service -> port ." Health Check: " . 
					$service -> healthChecks[0] -> type -> name . " Weight: " . $service -> groupReferences[0] -> weight . " Notes: " . $notes . "\n");
				}
			}
		}
	}
} catch(Exception $e) {
    echo "Unable to retrieve services: " . $e -> getMessage();
}

```

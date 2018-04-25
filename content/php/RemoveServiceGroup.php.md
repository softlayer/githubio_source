---
title: "RemoveServiceGroup.php"
description: "RemoveServiceGroup.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer"
tags:
    - "loadbalancers"
---


```
<?php
/**
 * This script removes a service group from a Load Balancer
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getAdcLoadBalancers
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer 
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer/dele
 * @see http://sldn.softlayer.com/article/Object-Filters
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

/**
 * Define the VIP Address from load balancer
 * @var string
 */
 $vipAddress = "159.253.157.82";

/**
 * Declare the port from service group that you wish to delete
 * @var int
 */
 $port = 5455;

// Create a SoftLayer API client object to the "SoftLayer_Account" and "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer" services
$accountService = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);
$serverService = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer', null, $username, $apiKey);

// Declare an object filter
$filter = new stdClass();
$filter -> adcLoadBalancers = new stdClass();
$filter -> adcLoadBalancers -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress -> operation = $vipAddress;
$accountService -> setObjectFilter($filter);

// Define an object mask, to get additional information for load balancer
$objectMask = "mask[virtualServerCount, virtualServers[serviceGroups[routingMethod, routingType]]]";
$accountService -> setObjectMask($objectMask);

try {
	// Get load balancer
	$loadBalancers = $accountService -> getAdcLoadBalancers();
	$errorFlag = true;
	
	foreach($loadBalancers[0] -> virtualServers as $virtualServer)
	{
		if($virtualServer -> port == $port)
		{
			$errorFlag = false;
			$serverService -> setInitParameter($virtualServer -> id);
		}		
	}
	if($errorFlag)
	{
		echo "There is not a service group with " . $port . " port.";
		return;
	}
	$result = $serverService -> deleteObject();
	echo "Has been removed the service group from load balancer? " . $result;
} catch(Exception $e) {
    echo "Unable to remove service group: " . $e -> getMessage();
}

```

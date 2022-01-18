---
title: "AddServiceGroup.php"
description: "AddServiceGroup.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method"
tags:
    - "loadbalancers"
---


```php
<?php
/**
 * This script adds a service group to Load Balancer. It is only necessary to specify the "Vip Address" from load balancer.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/e
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
 * @see http://sldn.softlayer.com/article/object-masks
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
 * Define the VIP Address from load balancer that you wish to cancel
 * @var string
 */
$vipAddress = "159.253.157.82";

/**
 * Define the new allocation for service group. The sum for all allocations should be 100 
 * (Including the new one that you wish to add).
 * @var array int
 */
$allocations = array(10, 10, 10, 70);

/**
 * Define parameters to add the service group
 * @var $group string
 * @var $method string
 * @var $port int
 * @var $notes string
 * @var $timeout int
 */
$group = "HTTPS";
$method = "Insert Cookie";
$port = 5459;
$notes = "this is for test Rcv";
$timeout = 0;

// Create a SoftLayer API client object to the "SoftLayer_Account", "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress",
// "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type" and "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method" services
$accountService = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);
$balancerService = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', null, $username, $apiKey);
$groupService = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type', null, $username, $apiKey);
$methodService = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method', null, $username, $apiKey);

// Declare an object filter
$filter = new stdClass();
$filter -> adcLoadBalancers = new stdClass();
$filter -> adcLoadBalancers -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress -> operation = $vipAddress;
$accountService -> setObjectFilter($filter);

// Declare an object filter, to get group id
$groupFilter = new stdClass();
$groupFilter -> name = new stdClass();
$groupFilter -> name -> operation = $group;
$groupService -> setObjectFilter($groupFilter);

// Declare an object filter, to get method id
$methodFilter = new stdClass();
$methodFilter -> name = new stdClass();
$methodFilter -> name -> operation = $method;
$methodService -> setObjectFilter($methodFilter);

// Define an object mask, to get additional information for load balancer
$objectMask = "mask[virtualServerCount, virtualServers[serviceGroups]]";
$accountService -> setObjectMask($objectMask);

try {
	// Get method an group information
	$methods = $methodService -> getAllObjects();
	$groups = $groupService -> getAllObjects();

	// Build a SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type object containing the group information
	$groupObject = new stdClass();
	$groupObject -> routingMethodId = $methods[0] -> id;
	$groupObject -> routingTypeId = $groups[0] -> id;
	$groupObject -> notes = $notes;
	$groupObject -> timeout = $timeout;
	$groupList = array();
	$groupList[] = $groupObject;

	// Build a SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method object
	$methodObject = new stdClass();
	$methodObject -> port = $port;
	$methodObject -> serviceGroups = $groupList;

	// Get Load Balancer
	$loadBalancers = $accountService -> getAdcLoadBalancers();

	// Add Method property to Virtual Servers from Load Balancer
	array_push($loadBalancers[0] -> virtualServers, $methodObject);

	// Setting init parameter
	$balancerService -> setInitParameter($loadBalancers[0] -> id);

	// Adding allocations for the service groups
	if (sizeof($allocations) == (($loadBalancers[0] -> virtualServerCount) + 1)) {
		if ($loadBalancers[0] -> virtualServerCount == 0) {
			$loadBalancers[0] -> virtualServers[0] -> allocation = $allocations[0];
		} else {
			for ($i = 0; $i <= $loadBalancers[0] -> virtualServerCount; $i++) {
				$loadBalancers[0] -> virtualServers[$i] -> allocation = $allocations[$i];
			}
		}
	} else {
		echo "Error: The number of allocations is not the required";
		return;
	}

	// Adding the service group
	$result = $balancerService -> editObject($loadBalancers[0]);
	echo "Has been added the service group to the Load Balancer?: " . $result;

} catch(Exception $e) {
	echo "Unable to add service group: " . $e -> getMessage();
}

```

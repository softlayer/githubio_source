---
title: "AddServiceToServiceGroup.php"
description: "AddServiceToServiceGroup.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet_IpAddress"
    - "SoftLayer_Account"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check_Type"
tags:
    - "loadbalancers"
---


```php
<?php
/**
 * This method adds a service into service group. It is only necessary to specify the "Vip Address" 
 * from load balancer and "Virtual Port" from the service group, to which you wish to add the service.
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
 * Define the VIP Address from load balancer that you wish to add a service
 * @var string
 */
$vipAddress = "173.193.117.96";

/**
 * Define the "Virtual Port" from service group, to which you wish to add the service
 * @var int
 */
$virtualPort = 80;
 
/**
 * Define parameters for the service that you wish to add
 * Note: The "Dest. Port" ($destPort) should not exist in the service group. If it exists, 
 * the service group which has the same "Dest. Port" will be edited.
 * 
 * @var $destinationIp string
 * @var $destPort int
 * @var $healthCheck string
 * @var $weight int
 * @var $notes string 
 */
 $destinationIp = "50.23.6.44";
 $destPort = 817;
 $healthCheck = "HTTP-CUSTOM";
 $weight = 99;
 $notes = "testRcv17";

/**
 * If you want to add a service with health check "HTTP-CUSTOM", you need to fill the below parameters:
 * @var $type string
 * @var $location string
 * @var $response string
 */
 $type = "GET";
 $location = "/index.php";
 $response = "error";

// Create a SoftLayer API client object to the "SoftLayer_Account", "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress",
// "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check_Type" and "SoftLayer_Network_Subnet_IpAddress" services
$accountService = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);
$balancerService = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', null, $username, $apiKey);
$healthCheckService = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check_Type', null, $username, $apiKey);
$ipService = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Subnet_IpAddress', null, $username, $apiKey); 

// Declare an object filter, to get Ip Address information
$filter = new stdClass();
$filter -> adcLoadBalancers = new stdClass();
$filter -> adcLoadBalancers -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress -> operation = $vipAddress;
$accountService -> setObjectFilter($filter);

// Declare an object filter, to get healthCheck information
$healthCheckFilter = new stdClass();
$healthCheckFilter -> name = new stdClass();
$healthCheckFilter -> name -> operation = $healthCheck;
$healthCheckService -> setObjectFilter($healthCheckFilter);

// Define an object mask, to get additional information for load balancer
$objectMask = "mask[virtualServers[serviceGroups[services[healthChecks[type], groups, groupReferences, ipAddress]]]]";
$accountService -> setObjectMask($objectMask);

try {
	// Get HealthCheck information
	$healthCheckObjects = $healthCheckService -> getAllObjects();
	
	// Get Ip Address information
	$ipAddress= $ipService -> findByIpv4Address($destinationIp); 
	
	// Build a SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress 
	// object containing the service information that you wish to add 
	$templateObject = new stdClass();
	$templateObject -> enabled = 1;
	$templateObject -> groupReferences = array(array("weight" => $weight));
	$templateObject -> healthChecks = array(array("healthCheckTypeId" => $healthCheckObjects[0] -> id));
	if($healthCheck == "HTTP-CUSTOM")
	{
		$templateObject -> healthChecks = array(array("healthCheckTypeId" => $healthCheckObjects[0] -> id, "attributes" => array(array("healthAttributeTypeId" => 22,
		 "value" => $type), array("healthAttributeTypeId" => 23, "value" => $location), array("healthAttributeTypeId" => 24, "value" => $response))));
	}
	$templateObject -> ipAddressId = $ipAddress -> id;
	$templateObject -> port = $destPort;
	$templateObject -> notes = $notes;
	
	// Get Load Balancer	
	$loadBalancers = $accountService -> getAdcLoadBalancers();
	foreach($loadBalancers[0] -> virtualServers as $virtualServer)
	{
		if($virtualServer -> port == $virtualPort)
		{
			// Adding the service to service group from load balancer
			array_push($virtualServer -> serviceGroups[0] -> services, $templateObject);
		}
	}
	
	// Setting init parameter
	$balancerService -> setInitParameter($loadBalancers[0] -> id);
	
	// Adding service to the service group
	$result = $balancerService -> editObject($loadBalancers[0]);
	echo "Has been added the service to the service group from load balancer?: " . $result;

} catch(Exception $e) {
	echo "Unable to add the service: " . $e -> getMessage();
}

```

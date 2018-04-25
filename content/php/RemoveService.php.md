---
title: "RemoveService.php"
description: "RemoveService.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service"
    - "SoftLayer_Account"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
tags:
    - "loadbalancers"
---


```
<?php
/**
* This method removes a service into service group. It is only necessary to specify the "Vip Address" 
 * from load balancer and "Virtual Port" from the service group and the "Dest. Port" from service that 
 * you wish to delete. This script allows to remove multiple services, you only need to specify the 
 * "Dest. Port" from services in $destPorts array.
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
 * Define the "VIP Address" from load balancer to which the service belongs to
 * @var string
 */
$vipAddress = "173.193.117.96";

/**
 * Define the "Virtual Port" to which the service belongs to
 * @var int
 */
$virtualPort = 80;

/**
 * Define the "Dest. Port" from the service or services that you wish to delete
 */
 $destPorts = array(815, 816, 817, 812, 80000, 8000);

// Create a SoftLayer API client object to the "SoftLayer_Account" and "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service" services
$accountService = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);
$serviceService = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service', null, $username, $apiKey);

// Declare an object filter
$filter = new stdClass();
$filter -> adcLoadBalancers = new stdClass();
$filter -> adcLoadBalancers -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress -> operation = $vipAddress;
$accountService -> setObjectFilter($filter);

// Define an object mask, to get additional information for load balancer
$objectMask = "mask[virtualServers[serviceGroups[services[healthChecks[type], groups, groupReferences, ipAddress]]]]";
$accountService -> setObjectMask($objectMask);

try {
	// Get Load Balancer
	$loadBalancers = $accountService -> getAdcLoadBalancers();
	
	foreach($loadBalancers[0] -> virtualServers as $virtualServer)
	{
		if($virtualServer -> port == $virtualPort)
		{
			foreach($virtualServer -> serviceGroups as $serviceGroup)
			{
				foreach($destPorts as $destPort)
				{
					$removeFlag = true;
					foreach($serviceGroup -> services as $service)					
					{
						if($service -> port == $destPort)
						{
							$serviceService -> setInitParameter($service -> id);
							$result = $serviceService -> deleteObject();
							echo "Has been the '" . $destPort . "' (Dest. Port) service deleted?: " . $result . "\n";
							$removeFlag = false;
						}
					}
					if($removeFlag)
					{
						echo "The ". $destPort . " Dest. Port doesn't exists.\n";
					}
				}
			}
		}
	}
	
} catch(Exception $e) {
	echo "Unable to remove the service: " . $e -> getMessage();
}


```

---
title: "StartSsl.php"
description: "StartSsl.php"
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
 * This script starts SSL. This action should be taken only after configuring an SSL certificate for the virtual IP.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getAdcLoadBalancers
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/s
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
 * Define the VIP Address from load balancer that you wish to start its SSL
 * @var string
 */
 $vipAddress = "50.23.117.127";

// Create a SoftLayer API client object to the "SoftLayer_Account" and "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress" services
$accountService = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);
$balancerService = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', null, $username, $apiKey);

// Declare an object filter
$filter = new stdClass();
$filter -> adcLoadBalancers = new stdClass();
$filter -> adcLoadBalancers -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress -> operation = $vipAddress;
$accountService -> setObjectFilter($filter);

try {
	$loadBalancers = $accountService -> getAdcLoadBalancers();
	
	// Setting init parameter
	$balancerService -> setInitParameter($loadBalancers[0] -> id);
		
	/**
	 * Start SSL
	 * If you want to Stop Ssl, use stopSsl() method.
	 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress-9
	 */
	 $result = $balancerService -> startSsl();
	 echo $result;
} catch(Exception $e) {
	echo "Unable to Start SSL: " . $e -> getMessage();
}

```

---
title: "GetSecurityCertificate.php"
description: "GetSecurityCertificate.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
    - "SoftLayer_Security_Certificate"
tags:
    - "loadbalancers"
---


```
<?php
/**
 * This script retrieves the SSL certificate currently associated with the VIP.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getAdcLoadBalancers
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress-6
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Security_Certificate
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
 * Define the VIP Address from load balancer that you wish to retrieve its Security Certificate
 * @var string
 */
 $vipAddress = "50.23.117.130";

// Create a SoftLayer API client object to the "SoftLayer_Account" and "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress" services
$accountService = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);
$balancerService  = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', null, $username, $apiKey);

// Declare an object filter
$filter = new stdClass();
$filter -> adcLoadBalancers = new stdClass();
$filter -> adcLoadBalancers -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress = new stdClass();
$filter -> adcLoadBalancers -> ipAddress -> ipAddress -> operation = $vipAddress;
$accountService -> setObjectFilter($filter);

try {
	// Get Load Balancer
	$loadBalancers = $accountService -> getAdcLoadBalancers();
	
	// Setting init parameters
	$balancerService -> setInitParameter($loadBalancers[0] -> id);	
	
	// Get Security Certificates
	$securityCertificate = $balancerService -> getSecurityCertificate();
	echo "Id: " . $securityCertificate -> id . " Certificate: " . $securityCertificate -> commonName . 
	"\nCertificate:  " . $securityCertificate -> certificate . "\nPrivate Key: " . $securityCertificate -> privateKey;
	
} catch(Exception $e) {
    echo "Unable to retrieve SSL Certificate: " . $e -> getMessage();
}

```

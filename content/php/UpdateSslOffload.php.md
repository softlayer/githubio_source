---
title: "UpdateSslOffload.php"
description: "UpdateSslOffload.php"
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
 * This script updates SSL Offload from load balancer.
 * It is only necessary to specify the VIP Address from load balancer and its options for SSL Offload as shown in Control Portal.
 * 
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getAdcLoadBalancers
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/e
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
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
 * Define the VIP Address from load balancer that you wish update its SSL Offload
 * @var string
 */
$vipAddress = "50.23.117.130";

/**
 * Define SSL offload properties
 * @var $certificate string
 * @var $enable boolean
 */
$certificate = "www.testssl.com";
$enable = true;

/**
 * Define the secure transport protocols enabled for this virtual IP address.
 * You must define at least one Protocol, if the certificate is enabled.
 * Protocols: SSLV3, TLSV1, TLSV12 and TLS_X
 */
$secureTransportProtocols = array("SSLV3", "TLSV12");

/**
 * Define the security ciphers enabled for this virtual IP address.
 * You must define at least one Cipher. if the certificate is enabled.
 * Ciphers: RC4-MD5, RC4-SHA, DES-CBC3-SHA, AES128-SHA, AES256-SHA, EXP-RC4-MD5 and EXP-DES-CBC-SHA
 */
$secureTransportCiphers = array("EXP-RC4-MD5", "RC4-SHA");

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

// Declare an object filter to get security certificate objet
$filterSsl = new stdClass();
$filterSsl -> securityCertificates = new stdClass();
$filterSsl -> securityCertificates -> commonName = new stdClass();
$filterSsl -> securityCertificates -> commonName -> operation = $certificate;

// Build a SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type object containing the group information
$templateObject = new stdClass();

try {
	// Declare a certificate flag to validate it
	$certificateFlag = false;
	// Verifying Security Certificate
	if($certificate == "No Certificate")
	{
			$templateObject -> securityCertificateId = null;
	}
	else{
		// Adding object filter, to get the security certificate
		$accountService -> setObjectFilter($filterSsl);
		// Get Security Certificate object
		$securityCertificates = $accountService -> getSecurityCertificates();
		
		if(sizeof($securityCertificates)>0)
		{
			foreach($securityCertificates as $ssl)
			{
				if($ssl -> validityDays > 0)
				{
					$templateObject -> securityCertificateId = $ssl -> id;
					$certificateFlag = true;
				}
			}
			if($enable)
			{
				// Setting Secure Transport Protocols		
				$protocols = array();
				if(sizeof($secureTransportProtocols)>0 && sizeof($secureTransportCiphers) >0)
				{
					foreach($secureTransportProtocols as $protocol)
					{
						$protocols[] = array("keyName"=> $protocol);
					}
					$templateObject -> secureTransportProtocols = $protocols;
				
					// Setting Secure Transport Ciphers			
					$ciphers = array();
					foreach($secureTransportCiphers as $cipher)
					{
						$ciphers[] = array("keyName" => $cipher);
					}	
					$templateObject -> secureTransportCiphers = $ciphers;
				}
				else{
					echo "You must define at least one item in 'Secure Transport Protocol' (\$secureTransportProtocols) and 'Secure Transport Ciphers' (\$secureTransportCiphers)";
					return;
				}
			}
		}else{
			echo $certificate . " certificate doesn't exists.";
			return;
		}
	} 
	// Setting an object filter, to get the load balancer object by VIP Address
	$accountService -> setObjectFilter($filter);
	// Get Load Balancer	
	$loadBalancers = $accountService -> getAdcLoadBalancers();
	// Setting init parameter
	$balancerService -> setInitParameter($loadBalancers[0] -> id);
	// Update SSL Offload
	$result = $balancerService -> editObject($templateObject);
	print_r("Has been updated the 'SSL Offload' from " . $vipAddress . " Load Balancer?: " . $result);
	// Enable/disable certificate
	if($certificateFlag == true)
	{
		if($enable)
		{
			$bool = $balancerService -> startSsl();
		}
		else
			{
				$bool = $balancerService -> stopSsl();
			}
	}
} catch(Exception $e) {
	echo "Unable to update Ssl Offload: " . $e -> getMessage();
}

```

---
title: "GetOverrides.php"
description: "GetOverrides.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
    - "SoftLayer_Network_Service_Vpn_Overrides"
    - "SoftLayer_SoapClient"
tags:
    - "vpnoverrides"
---


```
<?php
/**
 * Get Overrides
 * 
 * This script retrieves a portal user's vpn accessible subnets for users. It uses 
 * SoftLayer_User_Customer::getOverrides. You can retrieve the information like the following link 
 * displayed: https://control.softlayer.com/account/users (VPN Access >> SSL) 
 * 
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/getOverridesf
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Service_Vpn_Overrides
 * @see http://sldn.softlayer.com/article/Object-Masks
 * @see http://sldn.softlayer.com/article/Object-Filters
 * 
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com> 
 */
require_once dirname(__FILE__) . "/SoftLayer/SoapClient.class.php";

// Your SoftLayer API username.
$username = "set me";

// Your SoftLayer API key.
$key = "set me";

// Create a SoftLayer API client object for "SoftLayer_Account" and "SoftLayer_User_Customer" services
$userCustomer = SoftLayer_SoapClient::getClient("SoftLayer_User_Customer", null, $username, $key);
$account = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $key);

// Declare an array with the usernames from users that you wish to retrieve vpn accessible subnets.
$users = array("user1", "user2", "user3");

// Declare an object filter, to retrieve users with the specific username specified in "$users" array.
$filter = new stdClass();
$filter -> users = new stdClass();
$filter -> users -> username = new stdClass();
$filter -> users -> username -> operation = "in";
$filter -> users -> username -> options = array();
$filter -> users -> username -> options[0] = new stdClass();
$filter -> users -> username -> options[0] -> name = "data";
$filter -> users -> username -> options[0] -> value = $users;
$account -> setObjectFilter($filter);

// Get users 
$receiptUsers = $account -> getUsers();

// Define objectMask to retrieve subnet information
$userCustomer -> setObjectMask("mask[id, subnet[networkIdentifier, cidr, subnetType, networkVlan[primaryRouter]]]");

for ($i=0; $i < sizeof($receiptUsers); $i++) 
{
	// Set init parameter for user
	$userCustomer -> setInitParameter($receiptUsers[$i] -> id);
	try {
		$receiptOverrides = $userCustomer -> getOverrides();
		echo "Username:   " . $receiptUsers[$i] -> username;
		//Verify If there exists 0 vpn overrides.
		if(sizeof($receiptOverrides)==0)
		{
			echo "\nNo exists VPN overrides.";
		}
		else{
			echo "\nId          Subnet               Subnet Type           Routed To\n";			
		}
		for ($j=0; $j < sizeof($receiptOverrides); $j++) 
		{
			echo $receiptOverrides[$j] -> id . "      " .  $receiptOverrides[$j] -> subnet -> networkIdentifier . "/" .
			$receiptOverrides[$j] -> subnet -> cidr. "       " . $receiptOverrides[$j] -> subnet -> subnetType . "         " .
			$receiptOverrides[$j] -> subnet -> networkVlan -> vlanNumber . " " .  $receiptOverrides[$j] -> subnet -> networkVlan -> primaryRouter -> hostname . "\n";
		}
		echo "\n------------------------------------------------------------------\n";
		
	} catch(Exception $e)
	{
		echo "Unable to retrieve VPN overrides: " . $e -> getMessage();
	}
	
} 
```

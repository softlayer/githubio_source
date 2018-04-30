---
title: "CreateVpnOverrides.php"
description: "CreateVpnOverrides.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Vpn_Overrides"
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
 * Create VPN overrides 
 * 
 * This script creates VPN overrides for multiple users. It is necessary to specify the networkIdentifiers from 
 * subnets to create the overrides and the usernames from users which the overrides will be created.   
 * 
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Network_Service_Vpn_Overrides/createObjects
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Service_Vpn_Overrides
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/getOverrides
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

// Define the networks identifiers from subnets to create the overrides 
$subnets = array("10.90.148.192", "10.17.82.128", "10.28.168.64");

// Define the usernames from users that you wish to create the overrides
$users = array("user1", "user2", "user3");

// Create a SoftLayer API client object for "SoftLayer_Account" and "SoftLayer_Network_Vpn_Overrides" services
$client = SoftLayer_SoapClient::getClient("SoftLayer_Network_Service_Vpn_Overrides", null, $username, $key);
$account = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $key);

// Declare an object filter, to retrieve subnets specified in $subnets array
$filterSubnets = new stdClass();
$filterSubnets -> subnets = new stdClass();
$filterSubnets -> subnets -> networkIdentifier = new stdClass();
$filterSubnets -> subnets -> networkIdentifier -> operation = "in";
$filterSubnets -> subnets -> networkIdentifier -> options = array();
$filterSubnets -> subnets -> networkIdentifier -> options[0] = new stdClass();
$filterSubnets -> subnets -> networkIdentifier -> options[0] -> name = "data";
$filterSubnets -> subnets -> networkIdentifier -> options[0] -> value = $subnets;
$account -> setObjectFilter($filterSubnets);

// Get Subnets
$receiptSubnets = $account -> getSubnets();

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


// Define an array to Build the template with all SoftLayer_Network_Service_Vpn_Overrides objects to be deleted.
$overrides = array();

// Build the template
for ($i=0; $i < sizeof($receiptUsers); $i++) {
	for ($j=0; $j < sizeof($receiptSubnets) ; $j++) { 
		array_push($overrides, array("subnetId" => $receiptSubnets[$j] -> id, "userId" => $receiptUsers[$i] -> id));
	}
}

try {
	$result = $client -> createObjects($overrides);
	print_r("The VPN overrides were created?: " . $result);
} catch (Exception $e) {
	echo "Unable to create VPN overrides: " . $e -> getMessage();
	}


```

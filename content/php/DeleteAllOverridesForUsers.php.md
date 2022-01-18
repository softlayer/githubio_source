---
title: "DeleteAllOverridesForUsers.php"
description: "DeleteAllOverridesForUsers.php"
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


```php
<?php
/**
 * Delete all overrides for users 
 * 
 * This script deletes all overrides for multiple users. It uses SoftLayer_User_Customer::getOverrides to get all the overrides
 * for each user and SoftLayer_Network_Service_Vpn_Overrides::deleteObjects to delete.
 * 
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Network_Service_Vpn_Overrides/deleteObjects
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

// Define an array with usernames who will delete the overrides
$users = array("user1", "user2", "user3");

// Create a SoftLayer API client object for "SoftLayer_Account", "SoftLayer_User_Customer" and "SoftLayer_Network_Vpn_Overrides" services
$client = SoftLayer_SoapClient::getClient("SoftLayer_Network_Service_Vpn_Overrides", null, $username, $key);
$userCustomer = SoftLayer_SoapClient::getClient("SoftLayer_User_Customer", null, $username, $key);
$account = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $key);

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
for ($i=0; $i < sizeof($receiptUsers) ; $i++) {
	
	$userCustomer -> setInitParameter($receiptUsers[$i] -> id);
	$result = $userCustomer -> getOverrides();
	for ($j=0; $j <sizeof($result) ; $j++) { 
		array_push($overrides, array("id" => $result[$j] -> id));
	}
}

try {
	$result = $client -> deleteObjects($overrides);
	print_r("All VPN overrides were deleted?: " . $result);
} catch (Exception $e) {
	echo "Unable to delete all VPN overrides: " . $e -> getMessage();
}


```

---
title: "DeleteOverridesForUser.php"
description: "DeleteOverridesForUser.php"
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
 * Delete specific overrides for single user
 * 
 * It is only necessary to specify the username from user and the networkIdentifiers from overrides which wish to delete. 
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

// Define the username who will delete the overrides.
$user = "user1";

// Define an array with the networkIdentifiers from subnets that you wish to delete
$subnets = array("10.28.168.64");

// Create a SoftLayer API client object for "SoftLayer_Account", "SoftLayer_User_Customer" and "SoftLayer_Network_Vpn_Overrides" services
$client = SoftLayer_SoapClient::getClient("SoftLayer_Network_Service_Vpn_Overrides", null, $username, $key);
$userCustomer = SoftLayer_SoapClient::getClient("SoftLayer_User_Customer", null, $username, $key);
$account = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $key);

// Declare an object filter, to retrieve users with the specific username
$filter = new stdClass();
$filter -> users = new stdClass();
$filter -> users -> username = new stdClass();
$filter -> users -> username -> operation = "_=".$user;
$account -> setObjectFilter($filter);

// Get users 
$receiptUsers = $account -> getUsers();

// Declare an object filter, to retrieve subnets specified in $subnets array
$filterOverrides = new stdClass();
$filterOverrides -> overrides = new stdClass();
$filterOverrides -> overrides -> subnet = new stdClass();
$filterOverrides -> overrides -> subnet -> networkIdentifier = new stdClass();
$filterOverrides -> overrides -> subnet -> networkIdentifier -> operation = "in";
$filterOverrides -> overrides -> subnet -> networkIdentifier -> options = array();
$filterOverrides -> overrides -> subnet -> networkIdentifier -> options[0] = new stdClass();
$filterOverrides -> overrides -> subnet -> networkIdentifier -> options[0] -> name = "data";
$filterOverrides -> overrides -> subnet -> networkIdentifier -> options[0] -> value = $subnets;
$userCustomer -> setObjectFilter($filterOverrides);

// Define objectMask to retrieve information from subnets
$userCustomer -> setObjectMask("mask[subnet]");

// Set init parameter for user
$userCustomer -> setInitParameter($receiptUsers[0] -> id);

try {
    // Get vpn accessible subnets for the user
    $receiptOverrides = $userCustomer -> getOverrides();

    // Delete vpn accessible subnets
    $result = $client -> deleteObjects($receiptOverrides);
    print_r("The overrides were deleted?: " . $result);
} catch (Exception $e) {
    echo "Unable to delete VPN overrides: " . $e -> getMessage();
}

```

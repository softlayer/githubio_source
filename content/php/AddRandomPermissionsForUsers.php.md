---
title: "AddRandomPermissionsForUsers.php"
description: "AddRandomPermissionsForUsers.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
    - "SoftLayer_User_Customer_CustomerPermission_Permission"
tags:
    - "users"
---


```
<?php
/**
 * Add Random Permission for users
 *
 * This script adds permissions for specific usernames, you need to configure the usernames in the array $users.
 * All the permissions that you specified will be added to them. In this case we will generate randomly the permissions.
 * Also the script has attached an example for specific permissions in comments.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/addBulkPortalPermission
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_CustomerPermission_Permission/getAllObjects
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
 * @see http://sldn.softlayer.com/article/Object-Filters
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once ("C:/PhpSoftLayer/SoftLayer/SoftLayer/SoapClient.class.php");

/**
 * SoftLayer API username
 * @var string
 */
$username = "set me";

/**
 * SoftLayer API key
 * @var string
 */
$apiKey = "set me";

/**
 * Declare the usernames to add permissions.
 * @var array()
 */
$users = array("user1", "user2", "user3");

/*
 * Create SoftLayer API client object for
 * SoftLayer_User_Customer_CustomerPermission_Permission, SoftLayer_Account and SoftLayer_User_Customer
 */
$customerPermission = SoftLayer_SoapClient::getClient("SoftLayer_User_Customer_CustomerPermission_Permission", null, $username, $apiKey);
$account = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);
$userCustomer = SoftLayer_SoapClient::getClient("SoftLayer_User_Customer", null, $username, $apiKey);

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

// Get Users
$receiptUsers = $account -> getUsers();

// Get All existing permissions
$receipt = $customerPermission -> getAllObjects();

for ($i = 0; $i <= sizeof($receiptUsers) - 1; $i++) {
	/**
     * We will generate randomly the permissions for the users.
     * If you need to insert specific permissions, try the following:
     * E.g.
     *
     * $permissions =
     * array(array('keyName' => DNS_MANAGE),
     * array('keyName' => TICKET_VIEW_ALL));
     *
     * To Retrieve keyNames permissions, try the following method:
     * SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects
     */
     $permissions = array();
	 for ($j=0; $j <= rand(3, 10); $j++) {
	 	array_push($permissions, array("keyName" => $receipt[rand(1, 80)] -> keyName));
	 }
	 // Set init parameters for the user which the permits be added.
	 $userCustomer -> setInitParameter($receiptUsers[$i] -> id);
	 try {
	 	// Add Permissions to the user        
	 	$result = $userCustomer -> addBulkPortalPermission($permissions);
		// Print the result
        print_r("The following permissions were added for user " . $receiptUsers[$i] -> username . ":\n");
        for ($k = 0; $k < sizeof($permissions); $k++) {
            print_r("                         " . ($k + 1) . " " . $permissions[$k]["keyName"] . "\n");
        }
	 } catch(Exception $e) {
	 	print_r("Unable to add permissions for the users: " . $e -> getMessage());
	 }
}


```

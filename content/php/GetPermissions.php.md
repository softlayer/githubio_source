---
title: "GetPermissions.php"
description: "GetPermissions.php"
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
 * Get Permissions
 *
 * This script retrieves all permissions for multiple users. You need to specify all the users that you want
 * to retrieve permissions in $users array. This script uses SoftLayer_User_Customer::getPermisions
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/getPermissions
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

try {
    for ($i = 0; $i <= sizeof($receiptUsers) - 1; $i++) {

        // Set init parameters for the user which the permits be added.
        $userCustomer -> setInitParameter($receiptUsers[$i] -> id);
        // Add Permissions to the user
        $permissions = $userCustomer -> getPermissions();
        // Print the result
        print_r("Permissions for user " . $receiptUsers[$i] -> username . ":\n");
        for ($j = 0; $j < sizeof($permissions); $j++) {
            print_r("                                    " . ($j + 1) . " " . $permissions[$j] -> keyName . "\n");
        }
    }
} catch(Exception $e) {
    print_r("Unable to add permissions for the users: " . $e -> getMessage());
}

```

---
title: "AddAllPermissionsForUsers.php"
description: "AddAllPermissionsForUsers.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
    - "SoftLayer_User_Customer_CustomerPermission_Permission"
tags:
    - "users"
---


```php
<?php
/**
 * Add All Portal Permission for users
 *
 * This script adds all permissions from a portal user's permission set. In this case it adds for multiple users.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/addBulkPortalPermission
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
 * Declare the usernames to remove permissions
 * @var array()
 */
$users = array("user1", "user2", "user3");

/*
 * Create SoftLayer API client object for SoftLayer_Account, SoftLayer_User_Customer and 
 * SoftLayer_User_Customer_CustomerPermission_Permission services
 */
$account = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);
$client = SoftLayer_SoapClient::getClient("SoftLayer_User_Customer", null, $username, $apiKey);
$customerPermission = SoftLayer_SoapClient::getClient("SoftLayer_User_Customer_CustomerPermission_Permission", null, $username, $apiKey);

// Declare an object filter, to retrieve users with the specific usernames
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
// Get All Permissions
$permissions = $customerPermission -> getAllObjects();

for ($i = 0; $i < sizeof($receiptUsers); $i++) {
    // Set init parameters to the Client
    $client -> setInitParameter($receiptUsers[$i] -> id);
    try {
        /*
		 * Add permissions, if you want to remove all permissions for users, change the below line for:
		 * $result = $client -> removeBulkPortalPermission($permissions);
		 */
        $result = $client -> addBulkPortalPermission($permissions);
        // Print Result
        print_r("All permissions were added for " . $receiptUsers[$i] -> username . "?: " . $result . "\n");
    } catch(Exception $e) {
        echo "Unable to add all permissions for ". $receiptUsers[$i] -> username . ": ". $e -> getMessage();
    }
}

```

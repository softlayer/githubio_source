---
title: "RemovePermissionsForUsers.php"
description: "RemovePermissionsForUsers.php"
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
 * Remove Bulk Portal Permission for users
 *
 * This script removes multiple permissions from a portal user"s permission set. In this case it removes for multiple users.
 * You can retrieve the "keyName" permissions using SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects method.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/removeBulkPortalPermission
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
 * Create SoftLayer API client object for SoftLayer_Account and SoftLayer_User_Customer
 */
$account = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);
$client = SoftLayer_SoapClient::getClient("SoftLayer_User_Customer", null, $username, $apiKey);

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

/**
 * Set Permission template with the permissions to be removed from the users
 */
$permissions = array( array("keyName" => "TICKET_VIEW", "name" => "View Tickets"), 
array("keyName" => "ACCOUNT_SUMMARY_VIEW", "name" => "view account summary"), 
array("keyName" => "TICKET_SEARCH", "name" => "Search Tickets"), 
array("keyName" => "TICKET_ADD", "name" => "Add Tickets"), 
array("keyName" => "TICKET_VIEW_BY_HARDWARE", "name" => "View Tickets by Hardware Access"), 
array("keyName" => "TICKET_VIEW_BY_VIRTUAL_GUEST", "name" => "View Tickets by Computing Instance Access"), 
array("keyName" => "USER_MANAGE", "name" => "add / edit user"), 
array("keyName" => "ACCESS_ALL_HARDWARE", "name" => "Access all hardware"), 
array("keyName" => "ACCESS_ALL_GUEST", "name" => "Access all guests"));

for ($i = 0; $i < sizeof($receiptUsers); $i++) {
    // Set init parameters to the Client
    $client -> setInitParameter($receiptUsers[$i] -> id);
    try {
        $result = $client -> removeBulkPortalPermission($permissions);
        print_r("The permissions were removed for " . $receiptUsers[$i] -> username . " ?: " . $result . "\n");
    } catch(Exception $e) {
        print_r("Unable to remove permissions for " . $receiptUsers[$i] -> username . " :" . $e -> getMessage() . "\n");
    }
}

```

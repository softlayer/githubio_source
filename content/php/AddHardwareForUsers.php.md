---
title: "AddHardwareForUsers.php"
description: "AddHardwareForUsers.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
tags:
    - "users"
---


```
<?php
/**
 * Add Bulk Hardware Access
 *
 * This script adds multiple hardware to a portal user's hardware access list. This script works for multiple 
 * users and the users need to be able the permission: "View Hardware Details", you can set this in the following 
 * link: https://control.softlayer.com/account/users or using SoftLayer_User_Customer::addPortalPermission by API. 
 * This script works specifying just usernames from users and hostnames from hardware objects.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/addBulkHardwareAccess
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
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

// Declare users to allow access for Hardware objects
$users = array("user1", "user2", "user3");


// Declare hostnames from Hardware objects, to allow access from users
$hostnames = array("bms1", "bms2");

/*
 * Create SoftLayer API client object for SoftLayer_User_Customer and SoftLayer_Account services
 */
$client = SoftLayer_SoapClient::getClient("SoftLayer_User_Customer", null, $username, $apiKey);
$account = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);

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

// Declare an object filter, to retrieve users with the specific hostnames specified in "$hostnames" array.
$filter = new stdClass();
$filter -> hardware = new stdClass();
$filter -> hardware -> hostname = new stdClass();
$filter -> hardware -> hostname -> operation = "in";
$filter -> hardware -> hostname -> options = array();
$filter -> hardware -> hostname -> options[0] = new stdClass();
$filter -> hardware -> hostname -> options[0] -> name = "data";
$filter -> hardware -> hostname -> options[0] -> value = $hostnames;
$account -> setObjectFilter($filter);

// Get Hardware objects
$receiptHardware = $account -> getHardware();

// Declare array to store the ids from Hardware objects
$hardware = array();
for ($i = 0; $i < sizeof($receiptHardware); $i++) {
    array_push($hardware, $receiptHardware[$i] -> id);
}

// Allow for each user the access to Hardware objects
for ($i = 0; $i < sizeof($receiptUsers); $i++) {
    // Set init parameter
    $client -> setInitParameter($receiptUsers[$i] -> id);
    try {
        /*
         * If you want to remove the access just change the below line by this:
         * $result = $client -> removeHardwareAccess($hardware);
         */
        $result = $client -> addBulkHardwareAccess($hardware);
        // Print the result
        print_r("The user " . $receiptUsers[$i] -> username . " has access to Hardware objects?: " . $result . "\n");
    } catch(Exception $e) {
        print_r("Unable to allow access to Hardware for" . $receiptUsers[$i] -> username . ": " . $e -> getMessage() . "\n");
    }
}

```

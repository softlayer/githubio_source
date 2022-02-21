---
title: "AddVsiForUsers.php"
description: "AddVsiForUsers.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
tags:
    - "users"
---


```php
<?php
/**
 * Add Bulk Virtual Guest Access
 * 
 * This script adds multiple CloudLayer Computing Instances for multiple users to a portal user's access list.
 * The users needs to be able the permission: "View Virtual Server Details", you can set this in the following 
 * page: https://control.softlayer.com/account/users or using SoftLayer_User_Customer::addPortalPermission by API.
 * This script works specifying just usernames from users and hostnames from virtual guests. 
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/addBulkVirtualGuestAccess
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

/*
 * Create SoftLayer API client object for SoftLayer_User_Customer and SoftLayer_Account services
 */
$client = SoftLayer_SoapClient::getClient("SoftLayer_User_Customer", null, $username, $apiKey);
$account = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);

// Declare users to allow access for Virtual Guests
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

// Get Users
$receiptUsers = $account -> getUsers();

// Declare hostnames from Virtual Guests, to allow access from users
$hostnames = array("vsi1", "vsi2");

// Declare an object filter, to retrieve users with the specific hostnames specified in "$hostnames" array.
$filter = new stdClass();
$filter -> virtualGuests = new stdClass();
$filter -> virtualGuests -> hostname = new stdClass();
$filter -> virtualGuests -> hostname -> operation = "in";
$filter -> virtualGuests -> hostname -> options = array();
$filter -> virtualGuests -> hostname -> options[0] = new stdClass();
$filter -> virtualGuests -> hostname -> options[0] -> name = "data";
$filter -> virtualGuests -> hostname -> options[0] -> value = $hostnames;
$account -> setObjectFilter($filter);

// Get Virtual Guests
$receiptVsi = $account -> getVirtualGuests();

// Declare array to store the ids from Virtual Guests
$virtualGuests = array();
for ($i = 0; $i < sizeof($receiptVsi); $i++) {
    array_push($virtualGuests, $receiptVsi[$i] -> id);
}

// Allow for each user the access to Virtual Guests
for ($i = 0; $i < sizeof($receiptUsers); $i++) {
	// Set init parameter
    $client -> setInitParameter($receiptUsers[$i] -> id);
    try {
    	/*
		 * If you want to remove the access just change the below line by this:
		 * $result = $client -> removeBulkVirtualGuestAccess($virtualGuests); 
		 */	
    	$result = $client -> addBulkVirtualGuestAccess($virtualGuests);
		// Print the result
        print_r("The user ".$receiptUsers[$i] -> username . " has access to Virtual Guests?: " . $result . "\n");
    } catch(Exception $e) {
        print_r("Unable to allow access to Virtual Guests for" . $receiptUsers[$i] -> username . ": " . $e -> getMessage(). "\n");
    }
}

```

---
title: "GetDevicesAccess.php"
description: "GetDevicesAccess.php"
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
 * Get Devices Access
 *
 * This script retrieves all permissions for multiple users. You need to specify all the users that you want
 * to retrieve permissions in $users array. This script uses SoftLayer_User_Customer::getPermisions
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/getHardware
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/getVirtualGuests
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
 * Create SoftLayer API client object for SoftLayer_Account and SoftLayer_User_Customer services
 */
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

try {
    for ($i = 0; $i <= sizeof($receiptUsers) - 1; $i++) {
        // Set init parameters for the user which the permits be added.
        $userCustomer -> setInitParameter($receiptUsers[$i] -> id);
        // Retrieve Virtual Guests and Hardware objects with access allowed
        $virtualGuests = $userCustomer -> getVirtualGuests();
        $hardware = $userCustomer -> getHardware();
        // Print the result
        print_r("\nUser: " . $receiptUsers[$i] -> username);
        print_r("\n----------------------------------------------------------------------------------------\nHardware Objects:");
		for ($j=0; $j < sizeof($hardware); $j++) { 
			print_r("\n   ".($j+1)." Id: " .$hardware[$j] -> id. " FQDN: " . $hardware[$j] -> fullyQualifiedDomainName);
		}
		print_r("\nVirtual Guests:");
		for ($k=0; $k < sizeof($virtualGuests) ; $k++) { 
			print_r("\n   ".($k+1)." Id: " .$virtualGuests[$k] -> id. " FQDN: " . $virtualGuests[$k] -> fullyQualifiedDomainName);
		}
		print_r("\n----------------------------------------------------------------------------------------\n\n");
    }
} catch(Exception $e) {
    print_r("Unable to add permissions for the users: " . $e -> getMessage());
}

```

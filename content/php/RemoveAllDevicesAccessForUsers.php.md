---
title: "RemoveAllDevicesAccessForUsers.php"
description: "RemoveAllDevicesAccessForUsers.php"
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
 * Remove Devices Access for users
 *
 * This script removes all access for Virtual Guests and Hardware objects for specific users. 
 * This script makes API calls to SoftLayer_User_Customer::removeAllVirtualAccessForThisUser and 
 * SoftLayer_User_Customer::removeAllHardwareAccessForThisUser methods.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/removeAllVirtualAccessForThisUser
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/removeAllHardwareAccessForThisUser
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

for ($i = 0; $i < sizeof($receiptUsers); $i++) {
    // Set init parameters to the Client
    $client -> setInitParameter($receiptUsers[$i] -> id);
    try {
        // Remove Hardware objects access
        $resultHardware = $client -> removeAllHardwareAccessForThisUser();
        // Remove Virtual Guests access
        $resultVsi = $client -> removeAllVirtualAccessForThisUser();
        print_r("User: " . $receiptUsers[$i] -> username . "\n   All Hardware access removed?: " . $resultHardware . 
        "\n   All Virtual Guests access removed?: " . $resultVsi . "\n");
    } catch(Exception $e) {
        echo "Unable to remove access for ". $receiptUsers[$i] -> username . ": ". $e -> getMessage();
    }
}

```

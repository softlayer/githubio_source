---
title: "RemoveApiKeyForUsers.php"
description: "RemoveApiKeyForUsers.php"
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
 * Remove Api Authentication Key For Users
 * 
 * This script removes api authentication keys for usernames specified in $users array. 
 * This script uses the SoftLayer_User_Customer::removeApiAuthenticationKey method.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/removeApiAuthenticationKey
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
 * Declare the usernames to remove Api Authentication Keys.
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

// Declare an objectMask to retrieve the id from apiKey, because it is necessary to remove it.
$objectMask = "mask[apiAuthenticationKeys]";
$account -> setObjectMask($objectMask);

// Get Users
$receiptUsers = $account -> getUsers();

for ($i = 0; $i <= sizeof($receiptUsers) - 1; $i++) {
    // Set init parameters for the user which the api authentication key will be removed.
    $userCustomer -> setInitParameter($receiptUsers[$i] -> id);
    try {
        $result = $userCustomer -> removeApiAuthenticationKey($receiptUsers[$i] -> apiAuthenticationKeys[0] -> id );
        // Print the result
        print_r("The Api Key for user: " . $receiptUsers[$i] -> username . " was removed?: " . $result . "\n");
    } catch(Exception $e) {
        echo "Unable to remove Api Key for ".$receiptUsers[$i] -> username .": " . $e -> getMessage() ."\n";
    }
}

```

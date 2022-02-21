---
title: "AllowAccessFromHardware.php"
description: "AllowAccessFromHardware.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Network_Storage"
tags:
    - "networkstorage"
---


```php
<?php
/**
 * Allow Access From Hardware
 * 
 * This script allows access to Network Storage volume from a specified SoftLayer_Hardware object. 
 * It is only necessary to specify the username ($usernameStorage) from Network Storage and hostname ($hostname) 
 * from Hardware device.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkStorage
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage/allowAccessFromHardwareList
 * @see http://sldn.softlayer.com/article/Object-Filters
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once dirname(__FILE__) . "/SoftLayer/SoapClient.class.php";

/**
 * Your SoftLayer API username
 * @var string
 */
$username = "set me";

/**
 * Your SoftLayer API key
 * Generate one at: https://control.softlayer.com/account/users
 * @var string
 */
$apiKey = "set me";

/**
 * Declare hostname from Hardware which you wish to allow access
 * @var string
 */
$hostname = "hardwareHost";

/**
 * Declare username from Network Storage
 * @var string
 */
$usernameStorage = "SL01SV207819_1";

// Create a SoftLayer API client object to the "SoftLayer_Account" and "SoftLayer_Network_Storage" services
$client = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);
$storageService = SoftLayer_SoapClient::getClient("SoftLayer_Network_Storage", null, $username, $apiKey);

// Declare objectFilter, to get the Network Storage by username
$filterStorage = new stdClass();
$filterStorage -> networkStorage = new stdClass();
$filterStorage -> networkStorage -> username = new stdClass();
$filterStorage -> networkStorage -> username -> operation = "_=" . $usernameStorage;
$client -> setObjectFilter($filterStorage);

// Getting network storage
$storage = $client -> getNetworkStorage();

// Declare objectFilter, to get the Hardware by hostname
$filterHardware = new stdClass();
$filterHardware -> hardware = new stdClass();
$filterHardware -> hardware -> hostname = new stdClass();
$filterHardware -> hardware -> hostname -> operation = "_=" . $hostname;
$client -> setObjectFilter($filterHardware);

// Getting hardware object
$hardware = $client -> getHardware();

// Set the id from network storage as init parameter
$storageService -> setInitParameter($storage[0] -> id);

try {
	/**
	 * To remove access from Hardware, try the SoftLayer_Network_Storage::removeAccessFromHardwareList method.
	 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage/removeAccessFromHardwareList
	 * 
	 * Replace the line below with:
	 * $result = $storageService -> removeAccessFromHardwareList($hardware);
	 */
	$result = $storageService -> allowAccessFromHardwareList($hardware);
	print_r("Is Hardware access allowed: " . $result);

} catch(Exception $e) {
	echo "Unable to allow access from hardware: " . $e -> getMessage();
}

```

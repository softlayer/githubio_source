---
title: "GetDeviceSameLocationThanStorage.php"
description: "GetDeviceSameLocationThanStorage.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Network_Storage"
tags:
    - "networkstorage"
---


```
<?php
/**
 * Get Devices Same Location Than Storage
 *
 * This script retrieves all devices (Hardware and Virtual Guests) available in the same datacenter
 * than the Network Storage. It is only necessary to specify the username from Network Storage.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkStorage
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Storage
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
 * @see http://sldn.softlayer.com/article/Object-Masks
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
$apiKey = "set ne";

/**
 * Declare the username from the Network Storage
 * @var username
 */
$usernameStorage = "SL01SEL207819-5";

// Create a SoftLayer API client object to the "SoftLayer_Account" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);


// Declare objectMask to retrieve datacenter information from Network Storage
$client -> setObjectMask("mask[serviceResource[datacenter[name]]]");

// Declare an objectFilter to retrieve the storage with the same username
$filter = new stdClass();
$filter -> networkStorage = new stdClass();
$filter -> networkStorage -> username = new stdClass();
$filter -> networkStorage -> username -> operation = "_=" . $usernameStorage;
$client -> setObjectFilter($filter);

$result = $client -> getNetworkStorage();
print_r("Network Storage Id: " . $result[0] -> id . "   Username: " . $result[0] -> username . "   Datacenter: " . $result[0] -> serviceResource -> datacenter -> name);

// Declare objectFilter to retrieve Hardware devices
$filterHardware = new stdClass();
$filterHardware -> hardware = new stdClass();
$filterHardware -> hardware -> datacenter = new stdClass();
$filterHardware -> hardware -> datacenter -> name = new stdClass();

// Declare objectFilter to retrieve Virtual Guest devices
$filterVirtualGuests = new stdClass();
$filterVirtualGuests -> virtualGuests = new stdClass();
$filterVirtualGuests -> virtualGuests -> datacenter = new stdClass();
$filterVirtualGuests -> virtualGuests -> datacenter -> name = new stdClass();

try {
	// Adding datacenter from Network Storage for Hardware filter
    $filterHardware -> hardware -> datacenter -> name -> operation = "_=" . $result[0] -> serviceResource -> datacenter -> name;
	
	// Adding datacenter from Network Storage for Virtual Guest filter
    $filterVirtualGuests -> virtualGuests -> datacenter -> name -> operation = "_=" . $result[0] -> serviceResource -> datacenter -> name;

    // Set objectFilter and objectMask
    $client -> setObjectMask("mask[datacenter]");
    $client -> setObjectFilter($filterHardware);
	
	// Retrieve Hardware devices
    $hardwareResult = $client -> getHardware();
	print_r("\n\n*** Hardware ***\n");
    foreach ($hardwareResult as $hardware) {
        print_r("Id: " . $hardware -> id . "   FQDN: " . $hardware -> fullyQualifiedDomainName . "   Datacenter: " . $hardware -> datacenter -> name . "\n");
    }

    // Set objectFilter 
    $client -> setObjectFilter($filterVirtualGuests);
	
	// Retrieve Virtual Guest devices
    $virtualGuests = $client -> getVirtualGuests();
	print_r("\n*** Virtual Guest ***\n");
    foreach ($virtualGuests as $virtualGuest) {
        print_r("Id: " . $virtualGuest -> id . "   FQDN: " . $virtualGuest -> fullyQualifiedDomainName . "   Datacenter: " . $virtualGuest -> datacenter -> name . "\n");
    }
} catch(Exception $e) {
    echo "Unable to retrieve network storage and devices: " . $e -> getMessage();
}

```

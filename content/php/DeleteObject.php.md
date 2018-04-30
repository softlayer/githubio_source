---
title: "DeleteObject.php"
description: "DeleteObject.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
tags:
    - "virtualguest"
---


```
<?php
/**
 * Delete Virtual Guest
 *
 * This method will cancel a virtual guest by "hostname" using SoftLayer_Virtual_Guest::deleteObject method.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/deleteObject
 * @see http://sldn.softlayer.com/article/Object-Filters
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once "C:/Php/SoftLayer/SoftLayer/SoapClient.class.php";

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
 * Declare the hostname from Virtual Guest that you want to cancel, you can retrieve a list of them 
 * using: SoftLayer_Account::getVirtualGuests method.
 * @var string
 */
$hostname = "rcv2-test";

// Create a SoftLayer API client object for "SoftLayer_Account" and "SoftLayer_Virtual_Guest" services
$accountService = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);
$virtualGuestService = SoftLayer_SoapClient::getClient("SoftLayer_Virtual_Guest", null, $username, $apiKey);

// Declare an objectFilter to get the Virtual Guest with the host specified
$filter = new stdClass();
$filter -> virtualGuests = new stdClass();
$filter -> virtualGuests -> hostname = new stdClass();
$filter -> virtualGuests -> hostname -> operation = "_=" . $hostname;
$accountService -> setObjectFilter($filter);

try {
	// Getting account's associated virtual guest objects
    $virtualGuest = $accountService -> getVirtualGuests();
    // Setting of init parameter
    $virtualGuestService -> setInitParameter($virtualGuest[0] -> id);
    $result = $virtualGuestService -> deleteObject();
    print_r("Virtual Guest " . $virtualGuest[0] -> id . " - " . $hostname . " deleted?: " . $result);
} catch(Exception $e) {
    echo "Unable to delete Virtual Guest: " . $e -> getMessage();
}

```

---
title: "ReloadOperatingSystem.php"
description: "ReloadOperatingSystem.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Hardware_Server_Configuration"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_"
tags:
    - "virtualguest"
---


```
<?php
/**
 * Reload Operating System
 *
 * This script reloads current operating system configuration. It pass "FORCE" as the token parameter, 
 * in order to proceed with the reload without confirmation.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/reloadOperatingSystem
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Hardware_Server_Configuration
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
 * Declare Id from Virtual Guest to be edit
 * @var int
 */
$virtualId = 9477039;

/**
 * Declare the token as a confirmation to proceed with the reload, in this case we will use "FORCE",
 * to proceed the reload without confirmation.
 * @var string
 */
$token = "FORCE";

// Create a SoftLayer API client object for "SoftLayer_Virtual_Guest" services
$virtualGuestService = SoftLayer_SoapClient::getClient("SoftLayer_Virtual_Guest", null, $username, $apiKey);

/*
 * Define a collection of SoftLayer_Product_Item_Price objects. You can verify the item available for a given package using
 * SoftLayer_Product_Package::getItemPrices method
 */
$price = new stdClass();
$price -> id = 1742; // Windows Server 2008 Standard Edition SP2 (32bit)

$prices = array();
$prices[] = $price;

// Build skeleton SoftLayer_Container_hardware_Server_Configuration object with the new cloud configuration for the operating system reload
$config = new stdClass();
$config -> itemPrices = $prices;

// Setting up init parameter
$virtualGuestService -> setInitParameter($virtualId);

try {
    $result = $virtualGuestService -> reloadOperatingSystem($token, $config);
    print_r("Reload operating system for Virtual Guest: " . $virtualId . " ?: " . $result);
} catch(Exception $e) {
    echo "Unable to reload Operating System for Virtual Guest: " . $e -> getMessage();
}

```

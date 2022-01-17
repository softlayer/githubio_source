---
title: "DeletePersonRecords.php"
description: "DeletePersonRecords.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Account_Regional_Registry_Detail"
    - "SoftLayer_Account_Regional_Registry_Detail_Property"
    - "SoftLayer_SoapClient"
tags:
    - "rirregistration"
---


```php
<?php
/**
 * Delete Person Record
 *
 * This script deletes an existing person record with the same organization name specified. It makes a call 
 * to SoftLayer_Account::getSubnetRegistrationDetails method to get all of Subnet Registration Details and 
 * SoftLayer_Account_Regional_Registry_Detail::deleteObject method to delete a Person Record.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSubnetRegistrationDetails
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account_Regional_Registry_Detail/deleteObject
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
 * Declare Organization name of Person Record to be deleted
 * @var string
 */
$organizationName = "Organization orale";

// Create a SoftLayer API client object for "SoftLayer_Account" and
// "SoftLayer_Account_Regional_Registry_Detail" services
$accountService = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);
$regionalRegistryService = SoftLayer_SoapClient::getClient("SoftLayer_Account_Regional_Registry_Detail", null, $username, $apiKey);

// Define Object Mask to get "Properties" property
$accountService -> setObjectMask("mask[properties]");

// Define Object Filter to get only the Subnet Registration with the same organization name specified
$filter = new stdClass();
$filter -> subnetRegistrationDetails = new stdClass();
$filter -> subnetRegistrationDetails -> properties = new stdClass();
$filter -> subnetRegistrationDetails -> properties -> value = new stdClass();
$filter -> subnetRegistrationDetails -> properties -> value -> operation = "_=".$organizationName;
$accountService -> setObjectFilter($filter);

try {
    // Retrieve the Subnet Registration Detail with the same "Organization Name" specified
    $subnetRegistrations = $accountService -> getSubnetRegistrationDetails();
    // Setting init parameter to delete
    $regionalRegistryService -> setInitParameter($subnetRegistrations[0] -> id);
    $result = $regionalRegistryService -> deleteObject();
    echo "Id: " . $subnetRegistrations[0] -> id . " Organization name: " . $organizationName . " Deleted?: " . $result . "\n";
    
} catch(Exception $e) {
    echo "Unable to delete person record: " . $e -> getMessage();
}

```

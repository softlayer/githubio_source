---
title: "GetNetworkStorage.php"
description: "GetNetworkStorage.php"
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
 * Get Network Storages
 * 
 * This script retrieves an account's associated storage volumes. Also this script generates an CSV file with 
 * the information retrieved. The file is stored in "C:\Reports" (Windows OS) path by default, you can modify 
 * the "path" variable if you wish to change it.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkStorage
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Storage
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
$apiKey = "set me";

/**
 * Declare the "path" to create CSV file
 * @var string
 */
$path = "C:\Reports";

// Create a SoftLayer API client object to the "SoftLayer_Account" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);

// Define object mask to retrieve additional information from network storages 
$mask = "mask[username ,billingItem[id, category, location[longName]], storageType, serviceResourceBackendIpAddress, capacityGb, notes]";
$client -> setObjectMask($mask);

// Declare an objectFilter to retrieve only the storages with billingItem distinct from null
$filter = new stdClass();
$filter -> networkStorage = new stdClass();
$filter -> networkStorage -> billingItem = new stdClass();
$filter -> networkStorage -> billingItem -> operation = "NOT NULL";
$client -> setObjectFilter($filter);

// Define array for Network Storages to create CSV file
$storages = array();

try {
    // Get all network storages
    $result = $client -> getNetworkStorage();
    foreach ($result as $register) {
        print_r($register -> username . "     " . $register -> billingItem -> category -> name . "      " . $register -> storageType -> description . "      " . $register -> serviceResourceBackendIpAddress . "      " . $register -> capacityGb . "      " . $register -> billingItem -> location -> longName . "\n");
        array_push($storages, array($register -> username, $register -> billingItem -> category -> name, $register -> storageType -> description, $register -> serviceResourceBackendIpAddress, $register -> capacityGb, $register -> billingItem -> location -> longName));
    }

    // Declare titles for CSV file
    $titles = array("Volume Name", "Type", "Block/File Storage", "Hostname", "Capacity", "Location");
    // Create CSV file
    $dateTime = new DateTime();
    $date = $dateTime -> format("Y-m-d");
    $filePath = fopen($path . "\NetworkStorage" . $date . ".csv", "w");
    // Write titles in CSV file
    fputcsv($filePath, $titles);
    // Write all registers in CSV file
    foreach ($storages as $fields) {
        fputcsv($filePath, $fields);
    }
    // Close CSV file
    fclose($filePath);

} catch(Exception $e) {
    echo "Unable to get network storages: " . $e -> getMessage();
}

```

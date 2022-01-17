---
title: "GetRirRegistration.php"
description: "GetRirRegistration.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet_Registration"
    - "SoftLayer_Account"
    - "SoftLayer_Account_Regional_Registry_Detail"
    - "SoftLayer_SoapClient"
tags:
    - "rirregistration"
---


```php
<?php
/**
 * This script retrieves Subnet Registrations that are displayed in: https://control.softlayer.com/network/rir,
 * Additionally creates a CSV file with this information.
 * The file is stored in "C:\Reports" (Windows OS) path by default, you can modify "path" variable if you wish
 * to change it.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSubnetRegistrations
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_Registration
 * @see http://sldn.softlayer.com/article/Object-Masks
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
 * Declare the "path" to create CSV file
 * @var string
 */
$path = "C:\Reports";

// Create a SoftLayer API client object to the "SoftLayer_Account_Regional_Registry_Detail" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);

// Define object mask to get subnet, personDetails, regionalInternetRegistry and status from each register
$mask = "mask[registrations[personDetail[properties], status], regionalInternetRegistry]";
$client -> setObjectMask($mask);

// Declare an objectFilter to retrieve results avoiding subnet registers with "regionalInternetRegistry" to SoftLayer.
// These kind of registers are not displayed in "https://control.softlayer.com/network/rir"
$filter = new stdClass();
$filter -> subnets = new stdClass();
$filter -> subnets -> regionalInternetRegistry = new stdClass();
$filter -> subnets -> regionalInternetRegistry -> name = new stdClass();
$filter -> subnets -> regionalInternetRegistry -> name -> operation = "!~SoftLayer";
$client -> setObjectFilter($filter);

// Define array for Subnet Registrations to create CSV file
$registers = array();

try {
    // Get all Subnet registrations
    $result = $client -> getSubnets();
    foreach ($result as $register) {
        $id = $register -> id;
        $subnet = $register -> networkIdentifier . "/" . $register -> cidr;
        $status = "";
        $rir = $register -> regionalInternetRegistry -> name;
        $personRecord = " ";
        // Verify if the "status:name" property for each register is null, in order to replace it with "Unregistered" value
        if (isset($register -> registrations[0] -> status -> name) == NULL) {
            $status = "Unregistered";
        } else {
            // Get current status name from Subnet Registration
            $status = $register -> registrations[0] -> status -> name;
            // Verifying if each register has properties. There exists some cases that a subnet registration doesn't have properties added.
            if (isset($register -> registrations[0] -> personDetail -> properties) != NULL) {
                for ($i = 0; $i < sizeof($register -> registrations[0] -> personDetail -> properties); $i++) {
                    // Getting property type 61 that corresponds to "Organization" parameter
                    if (($register -> registrations[0] -> personDetail -> properties[$i] -> propertyTypeId) == 61) {
                        // Assign "Organization Name" to the person record variable
                        $personRecord = $register -> registrations[0] -> personDetail -> properties[$i] -> value;
                    }
                }
            }
        }
        // Print result
        echo("Id: " . $id . "\nSubnet: " . $subnet . "\nStatus Name: " . $status . "\nRIR: " . $rir . "\nPerson Record: " . $personRecord);
        // Add to "registers" array which will be used to generate CSV file.
        array_push($registers, array($subnet, $status, $rir, $personRecord));
        echo("\n------------------------------------------------------------------------------------\n");
    }
    // Declare titles for CSV file
    $titles = array("Subnet", "Status", "RIR", "Person Record");
    // Create CSV file
    $dateTime = new DateTime();
    $date = $dateTime -> format("Y-m-d");
    $filePath = fopen($path . "\SubnetRegistrations_" . $date . ".csv", "w");
    // Write titles in CSV file
    fputcsv($filePath, $titles);
    // Write all registers in CSV file
    foreach ($registers as $fields) {
        fputcsv($filePath, $fields);
    }
    // Close CSV file
    fclose($filePath);
} catch(Exception $e) {
    echo "Unable to get Subnet Registrations: " . $e -> getMessage();
}

```

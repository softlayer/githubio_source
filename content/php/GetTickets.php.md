---
title: "GetTickets.php"
description: "GetTickets.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Ticket"
tags:
    - "ticket"
---


```
<?php
/**
 * Get Tickets
 *
 * This script retrieves an account's associated tickets. The status for the tickets are: Assigned,
 * Open or Closed, you can get for one, two or all of them.
 *
 * The tickets are displayed with the same parameters displayed in https://control.softlayer.com/support/tickets.
 * Also this script generates an CSV file with the information retrieved. The file is stored in "C:\Reports" 
 * (Windows OS) path by default, you can modify the "path" variable if you wish to change it.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getTickets
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket
 * @see http://sldn.softlayer.com/article/Object-Filters
 * @see http://sldn.softlayer.com/article/Object-Masks
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

// Create a SoftLayer API client object to the "SoftLayer_Account" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);

// Define object mask to get Group, AssignedUser and AttachedHardwareCount parameters from ticket
$mask = "mask[id, title, lastEditType, attachedHardwareCount, lastEditDate, group[name], assignedUser[username], status[name]]";
$client -> setObjectMask($mask);

// Define the status to retrieve tickets
$status = array("Assigned", "Open", "Closed");

// Declare an object filter
$filter = new stdClass();
$filter -> tickets = new stdClass();
$filter -> tickets -> status = new stdClass();
$filter -> tickets -> status -> name = new stdClass();
$filter -> tickets -> status -> name -> operation = "in";
$filter -> tickets -> status -> name -> options = array();
$filter -> tickets -> status -> name -> options[0] = new stdClass();
$filter -> tickets -> status -> name -> options[0] -> name = "data";
$filter -> tickets -> status -> name -> options[0] -> value = $status;
$client -> setObjectFilter($filter);

// Define array for tickets to create CSV file
$csvTickets = array();

try {
    // Get Tickets
    $tickets = $client -> getTickets();
    foreach ($tickets as $ticket) {
        echo "Ticket #: " . $ticket -> id . "\nGroup: " . $ticket -> group -> name . "\nSubject/Title: " . $ticket -> title . "\nOwner: " . $ticket -> assignedUser -> username . "\nLast Replied: " . $ticket -> lastEditType . "\nDevice: " . $ticket -> attachedHardwareCount . " Device(s)" . "\nUpdated: " . $ticket -> lastEditDate;
        // Add information from each ticket to csv array
        array_push($csvTickets, array($ticket -> id, $ticket -> group -> name, $ticket -> title, $ticket -> assignedUser -> username, $ticket -> lastEditType, $ticket -> attachedHardwareCount, $ticket -> lastEditDate));
        echo("\n------------------------------------------------------------------------------------\n");
    }
    echo "Tickets: " . sizeof($tickets);
} catch(Exception $e) {
    echo "Unable to get tickets: " . $e -> getMessage();
}
try {
    // Get dateTime to create the CSV file
    $dateTime = new DateTime();
    // Convert dateTime to the following format "2015-06-11"
    $date = $dateTime -> format("Y-m-d");
    // Declare titles for CSV file
    $titles = array("Ticket #", "Group", "Subject/Title", "Owner", "Last Replied", "Device", "Updated");
    // Create csv file
    $filePath = fopen($path . "\Tickets_" . $date . ".csv", "w");
    // Write titles in CSV file
    fputcsv($filePath, $titles);
    // Write all registers in CSV file
    foreach ($csvTickets as $fields) {
        fputcsv($filePath, $fields);
    }
    // Close CSV file
    fclose($filePath);
    echo "\nCSV created in " . $path;
} catch(Exception $e) {
    echo "Unable to create CSV: " . $e -> getMessage();
}

```

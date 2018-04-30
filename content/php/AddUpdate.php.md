---
title: "AddUpdate.php"
description: "AddUpdate.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Container_Utility_File_Attachment"
    - "SoftLayer_Ticket_Update"
    - "SoftLayer_Ticket"
tags:
    - "ticket"
---


```
<?php
/**
 * Add Update
 *
 * This script adds an update to a ticket. A ticket update's entry has a maximum length of 4000 characters.
 * Also this script attaches two files to the Ticket (It cannot be add more than 2 files).
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/addUpdate
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket_Update
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Utility_File_Attachment
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
 * Declare the ticket id to add update
 * @var int
 */
$ticketId = 18830750;

/**
 * Define the file names for the file attachments 
 * @var string $filename
 * @var string $filenameTwo
 */
$filename = "file1.jpg";
$filenameTwo = "file2.jpg";
 
// Open and read the file #1 to attach
$path = "C:/Users/Ruber Cuellar/Pictures/allow.jpg";
$handle = fopen($path, "rb");
$data = fread($handle, filesize($path));
fclose($handle);

// Open and read the file #2 to attach
$pathTwo = "C:/Users/Ruber Cuellar/Pictures/download.png";
$handleTwo = fopen($pathTwo, "rb");
$dataTwo = fread($handleTwo, filesize($pathTwo));
fclose($handleTwo);

// Create SoftLayer API client object for "SoftLayer_Ticket" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Ticket", null, $username, $apiKey);

// Declare init parameter from the ticket to add the update
$client -> setInitParameter($ticketId);

// Build a skeleton SoftLayer_Ticket object containing the data of the ticket to be updated.
$templateObject = new stdClass();
$templateObject -> entry = "This is for test Update Entry";

// Build two skeleton SoftLayer_Container_Utility_File_Attachment objects containing the data for the files to be updated
$fileAttachment = new stdClass();
$fileAttachment -> data = $data;
$fileAttachment -> filename = $filename;

$fileAttachmentTwo = new stdClass();
$fileAttachmentTwo -> data = $dataTwo;
$fileAttachmentTwo -> filename = $filenameTwo;

// Declare an Array  of no more than two files to be updated in the ticket
$attachment = array($fileAttachment, $fileAttachmentTwo);

try {
    $result = $client -> addUpdate($templateObject, $attachment);
    print_r($result);
} catch(Exception $e) {
    echo "Unable to add update: " . $e -> getMessage();
}

```

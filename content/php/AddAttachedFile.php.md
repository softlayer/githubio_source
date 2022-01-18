---
title: "AddAttachedFile.php"
description: "AddAttachedFile.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Ticket_Attachment_File"
    - "SoftLayer_Container_Utility_File_Attachment"
    - "SoftLayer_Ticket"
tags:
    - "ticket"
---


```php
<?php
/**
 * Add Attached File
 *
 * This script attaches the given file to an existing SoftLayer Ticket. The format file could be: jpg, png, txt.
 * File attachments to tickets must have a unique name.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/addAttachedFile
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Utility_File_Attachment
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket_Attachment_File
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
 * Declare the ticket id to add attached file
 * @var int
 */
$ticketId = "18830750";

/**
 * Declare file name for the attached file
 * @var string
 */
$file = "allow2.jpg";

// Open and read the file
$filename = "C:/Users/Ruber Cuellar/Pictures/allow.jpg";
$handle = fopen($filename, "rb");
$data = fread($handle, filesize($filename));
fclose($handle);

// Create a SoftLayer API client object for "SoftLayer_Ticket" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Ticket", null, $username, $apiKey);

// Declare init parameter from the ticket to attach the file
$client -> setInitParameter($ticketId);

// Build a skeleton SoftLayer_Container_Utility_File_Attachment object containing the data for the file to attach
$fileAttachment = new stdClass();
$fileAttachment -> data = $data;
$fileAttachment -> filename = $file;

try {
    $result = $client -> addAttachedFile($fileAttachment);
    print_r($result);
} catch(Exception $e) {
    echo "Unable to add attached file: " . $e -> getMessage();
}

```

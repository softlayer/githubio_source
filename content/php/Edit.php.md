---
title: "Edit.php"
description: "Edit.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Container_Utility_File_Attachment"
    - "SoftLayer_Ticket"
tags:
    - "ticket"
---


```
<?php
/**
 * Edit Ticket
 *
 * This script edits a ticket created, in this case it edits assignedUser and 
 * notifyUserOnUpdateFlag, also it adds a content for the edited
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/edit
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket
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
 * Declare id of the ticket to edit
 * @var int
 */
$ticketId = 18833750;

/**
 * Declare parameters for the ticket
 * @var int $assignedUserId
 * @var boolean $notifyUserOnUpdateFlag
 * @var string $contents
 */
$assignedUserId = 126704;
$notifyUserOnUpdateFlag = true;
$contents = "Ticket Edited";

// Create SoftLayer API client object for "SoftLayer_Ticket" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Ticket", null, $username, $apiKey);

// Declare init parameter from the ticket to edit
$client -> setInitParameter($ticketId);

// Build a skeleton SoftLayer_Ticket object containing the data of the ticket to be edited.
$templateObject = new stdClass();
$templateObject -> assignedUserId = $assignedUserId;
$templateObject -> notifyUserOnUpdateFlag = $notifyUserOnUpdateFlag;

// Add contents for the ticket to be edited

try {
    $result = $client -> edit($templateObject, $contents);
    print_r($result);
} catch(Exception $e) {
    echo "Unable to edit the ticket: " . $e -> getMessage();
}

```

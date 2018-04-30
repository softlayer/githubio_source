---
title: "CreateStandardTicket.php"
description: "CreateStandardTicket.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Container_Utility_File_Attachment"
    - "SoftLayer_Ticket"
    - "SoftLayer_SoapClient"
tags:
    - "ticket"
---


```
<?php
/**
 * Create Standard Ticket
 *
 * This script creates a standard support ticket and It is assigned to master User. 
 * The ticket is created with the subject Id:1001 (Accounting Request)
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/createStandardTicket
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
 * Declare parameters for the ticket
 * @var string $contents
 * @var int $attachmentId
 * @var string $rootPassword
 * @var string $controlPanelPassword
 * @var string $accessPort
 * @var string $attachmentType
 * @var int $subjectId
 * @var string $title 
 */
$contents = "This is for test";
$attachmentId = null;
$rootPassword = "";
$controlPanelPassword = "";
$accessPort = "";
$attachmentType = "";
$subjectId = 1001;
$title = "This is for test";

// Create a SoftLayer API client object for "SoftLayer_Account" and "SoftLayer_Ticket" services
$accountService = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);
$ticketService = SoftLayer_SoapClient::getClient("SoftLayer_Ticket", null, $username, $apiKey);

// Get Id for the Master User
$accountService -> setObjectMask("mask[masterUser]");
$account = $accountService -> getObject();

// Build a skeleton SoftLayer_Ticket object containing the data of the ticket to submit.
$templateObject = new stdClass();
$templateObject -> assignedUserId = $account -> masterUser -> id;
$templateObject -> subjectId = $subjectId;
$templateObject -> title = $title;

try {
    $standardTicket = $ticketService -> createStandardTicket($templateObject, $contents, $attachmentId, $rootPassword, $controlPanelPassword, $accessPort, $attachmentType);
    print_r($standardTicket);
} catch(Exception $e) {
    echo "Unable to create standard ticket: " . $e -> getMessage();
}

```

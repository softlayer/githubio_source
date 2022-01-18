---
title: "AddAttachedAdditionalEmails.php"
description: "AddAttachedAdditionalEmails.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Ticket"
tags:
    - "ticket"
---


```php
<?php
/**
 * Add Attached Additional E-mails
 *
 * This script creates new additional email addresses for ticket created.  
 * These e-mails receive a notification when the ticket is updated.  
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/addAttachedAdditionalEmails
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
 * Declare the ticket id to add additional e-mails
 * @var int
 */
$ticketId = 18830750;

// Create a SoftLayer API client object for "SoftLayer_Ticket" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Ticket", null, $username, $apiKey);

// Declare init parameter from the ticket to add additional emails
$client -> setInitParameter($ticketId);

// Declare an array of email addresses to notify when the ticket is updated
$emails = array("noreply@softlayer.com", "noreply2@softlayer.com", "noreply3@softlayer.com");

try {
    $result = $client -> addAttachedAdditionalEmails($emails);
    print_r($result);
} catch(Exception $e) {
    echo "Unable to add additional emails: " . $e -> getMessage();
}

```

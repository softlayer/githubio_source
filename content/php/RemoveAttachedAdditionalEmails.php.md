---
title: "RemoveAttachedAdditionalEmails.php"
description: "RemoveAttachedAdditionalEmails.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Ticket"
tags:
    - "ticket"
---


```
<?php
/**
 * Remove Attached Additional E-mails
 *
 * This script removes email addresses from a ticket's notification list. If one of the provided email 
 * addresses is not attached to the ticket the method ignores it and continues to the next one. 
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/removeAttachedAdditionalEmails
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
 * Declare the id of the ticket to remove additional e-mails
 * @var int
 */
$ticketId = 20001985;

/**
 * Declare an array of email addresses to remove
 * @var array(string)
 */
$emails = array("noreply@softlayer.com", "noreply2@softlayer.com", "noreply3@softlayer.com");

// Create a SoftLayer API client object for "SoftLayer_Ticket" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Ticket", null, $username, $apiKey);

// Declare init parameter from the ticket to remove additional e-mails
$client -> setInitParameter($ticketId);

try {
    $result = $client -> removeAttachedAdditionalEmails($emails);
    print_r($result);
} catch(Exception $e) {
    echo "Unable remove additional e-mails: " . $e -> getMessage();
}

```

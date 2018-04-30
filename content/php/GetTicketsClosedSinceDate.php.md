---
title: "GetTicketsClosedSinceDate.php"
description: "GetTicketsClosedSinceDate.php"
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
 * Get Tickets Closed Since Date
 *
 * Retrieve all tickets closed since a given date.
 *  
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/getTicketsClosedSinceDate
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once 'C:/Php/SoftLayer/SoftLayer/SoapClient.class.php';

/**
 * Your SoftLayer API username
 * @var string
 */
$username = 'set me';

/**
 * Your SoftLayer API key
 * Generate one at: https://control.softlayer.com/account/users
 * @var string
 */
$apiKey = 'set me';

/**
 * Define string with date since that you want to retrieve closed tickets
 * Format 'M/d/Y H:i:s'
 * @var string
 */
$date = '06/11/2015 19:00:02';

// Create a SoftLayer API client object to the "SoftLayer_Ticket" service
$client = SoftLayer_SoapClient::getClient('SoftLayer_Ticket', null, $username, $apiKey);

// Declare an Object Mask to get assignedUserId username and status name
$client -> setObjectMask("mask[assignedUser[username], status[name]]");

try {
    $tickets = $client -> getTicketsClosedSinceDate(strtotime($date));
	print_r($tickets);
} catch(Exception $e) {
    echo 'Unable to get tickets closed: ' . $e -> getMessage();
}

```

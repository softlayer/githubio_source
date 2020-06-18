---
title: "Working with Tickets"
description: "A few examples on interacting with Tickets"
date: "2020-06-15"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Ticket"
tags:
    - "tickets"
---

Create Standard Ticket

Create a standard support ticket. Use a standard support ticket if you need to work out a problem related to 
SoftLayer's hardware, network, or services
```
<?php

require_once './vendor/autoload.php';

$username = "set me";
$apiKey = "set me";

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

Create Administrative Ticket

Create an administrative support ticket. Use an administrative ticket if you require SoftLayer's assistance managing 
your server or content.
```
<?php

require_once './vendor/autoload.php';

$username = "set me";
$apiKey = "set me";

$contents = "This is for test";
$attachmentId = null;
$rootPassword = "";
$controlPanelPassword = "";
$accessPort = "";
$attachmentType = "";
$title = "This is an Administrative Ticket for test";

// Create a SoftLayer API client object for "SoftLayer_Account" and "SoftLayer_Ticket" services
$accountService = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);
$ticketService = SoftLayer_SoapClient::getClient("SoftLayer_Ticket", null, $username, $apiKey);

// Get Id for the Master User
$accountService -> setObjectMask("mask[masterUser]");
$account = $accountService -> getObject();

// Build a skeleton SoftLayer_Ticket object containing the data of the ticket to submit.
$templateObject = new stdClass();
$templateObject -> assignedUserId = $account -> masterUser -> id;
$templateObject -> title = $title;

try {
    $administrativeTicket = $ticketService -> createAdministrativeTicket($templateObject, $contents, $attachmentId, $rootPassword, $controlPanelPassword, $accessPort, $attachmentType);
    print_r($administrativeTicket);
} catch(Exception $e) {
    echo "Unable to create an administrative ticket: " . $e -> getMessage();
}

```

Get tickets using an objectFilter

Pulls down all the tickets created after a set date, and lasted update was by an employee of SoftLayer. 
```
<?php

require_once './vendor/autoload.php';

$apiUsername = "set me";
$apiKey = "set me";


$startDate = new DateTime('2015-05-28T10:05:25-06:00');

$ticketClient = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $apiUsername, $apiKey);
$filter = new stdClass();
$filter->tickets = new stdClass();
$filter->tickets->updates = new stdClass();
$filter->tickets->updates->createDate = new stdClass();
$filter->tickets->updates->createDate->operation = 'greaterThanDate';
$filter->tickets->updates->createDate->options = array();
$filter->tickets->updates->createDate->options[0] = new stdClass();
$filter->tickets->updates->createDate->options[0]->name = 'date';
$filter->tickets->updates->createDate->options[0]->value = array($startDate->format('m/d/Y H:i:s'));
$filter->tickets->updates->editorType = new stdClass();
$filter->tickets->updates->editorType->operation = 'EMPLOYEE';

$mask = new \SoftLayer\Common\ObjectMask();;
$mask->tickets->updates;

$ticketClient->setObjectMask($mask);
$ticketClient->setObjectFilter($filter);

try {

  $updates = $ticketClient->getTickets();
  print_r($updates);

 } catch(Exception $e) {
     echo 'Cannot get the tickets: ' . $e->getMessage();
}

//prints out some SOAP debugging
print_r($ticketClient->__getLastRequest());

?>
```

Get Tickets Closed Since Date

Retrieve tickets closed since a given date. 
```
<?php

require_once './vendor/autoload.php';

$username = 'set me';
$apiKey = 'set me';

/**
 * Define string with date since that you want to retrieve closed tickets
 * Format 'M/d/Y H:i:s'
 * @var string
 */
$date = '06/11/2015 19:00:02';

$client = SoftLayer_SoapClient::getClient('SoftLayer_Ticket', null, $username, $apiKey);

$client -> setObjectMask("mask[assignedUser[username],status[name]]");

try {
    $tickets = $client -> getTicketsClosedSinceDate(strtotime($date));
	print_r($tickets);
} catch(Exception $e) {
    echo 'Unable to get tickets closed: ' . $e -> getMessage();
}

```


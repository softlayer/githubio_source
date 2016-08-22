---
title: "Creating a support ticket"
description: "Create a standard support ticket assigned to your user"
date: "2016-02-09"
classes: ["SoftLayer_Ticket_Subject", "SoftLayer_Ticket"]
tags:
    - "ticket"
---

Standard support tickets' titles must be selected from a pre-determined list of ticket subjects, defined in the [SoftLayer_Ticket_Subject](http://sldn.softlayer.com/reference/services/SoftLayer_Ticket_Subject) service. The following example will output all of the Ticket Subjects:

```php
<?php

/* You can use the getenv() module to pull your exported Username
and API key to keep from having to store them in your files */

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');

$client = \SoftLayer\SoapClient::getClient('SoftLayer_Ticket_Subject', null, $apiUsername, $apiKey);
$subjects = $client->getAllObjects();

print_r($subjects);
?>

```

Once you have the Ticket Subject ID you can pass it to [createStandardTicket](http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/createStandardTicket). In the following example we are opening a ticket under the subject Hardware Firewall Question (ID 1121).

```php
<?php

/* You can use the getenv() module to pull your exported Username
and API key to keep from having to store them in your files */

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');

$template = new stdClass();
$template->subjectId = 1121;
$template->assignedUserId = 123456;

$content = "Content of the ticket goes here";

$created_ticket = \SoftLayer\SoapClient::getClient('SoftLayer_Ticket', null, $apiUsername, $apiKey);
$response = $created_ticket->createStandardTicket($template, $content);

print_r($response);

?>
```

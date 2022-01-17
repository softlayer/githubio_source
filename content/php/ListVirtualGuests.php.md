---
title: "ListVirtualGuests.php"
description: "ListVirtualGuests.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
tags:
    - "virtualguest"
---


```php
<?php
/**
 * List Virtual Guests.
 * It retrieves an account's associated virtual guest objects.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

// Your SoftLayer API username.
$apiUsername = 'set me';

// Your SoftLayer API key.
$apiKey = 'set me';

// Set the service to use.
$serviceName ='SoftLayer_Account';

// Create a client to the SoftLayer_Account API service.
$client = SoftLayer_SoapClient::getClient($serviceName, null, $apiUsername, $apiKey);

// Declare an object filter to retrieve valid virtual guests.
$filter = new stdClass();
$filter->virtualGuests = new stdClass();
$filter->virtualGuests->host = new stdClass();
$filter->virtualGuests->host->operation = new stdClass();
$filter->virtualGuests->host->operation = "not null";

$client->setObjectFilter($filter);

try {
    $instanceList = $client->getVirtualGuests();
    print_r( $instanceList);
} catch(Exception $e) {
    echo "Unable to list the Virtual Guests: " . $e -> getMessage();
}

```

---
title: "Create a new virtual server with all options"
description: "Creates a new virtual server (VSI) and demonstrates the many options that can be used to customize the creation."
date: "2016-09-01"
classes:
  - "SoftLayer_Virtual_Guest"
tags:
  - "vsis"
  - "create"
---

```php

<?php

/* You can use the getenv() module to pull your exported Username
and API key to keep from having to store them in your files */

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');

$template = new stdClass();
$template->location = 1441195;
$template->datacenter->name = 'dal10';
$template->domain = 'example.com';
$template->startCpus = 2;
$template->maxMemory = 2048;
$template->operatingSystemReferenceCode = 'CENTOS_6_64';
$template->hostname = 'testphp';
$template->localDiskFlag = True;
$template->hourlyBillingFlag = True;
$template->dedicatedAccountHostOnlyFlag = False;
$template->primaryBackendNetworkComponent = 1286783;
$template->primaryNetworkComponent = 1286781;
$template->privateNetworkOnlyFlag = False;

try {
  $client = \SoftLayer\SoapClient::getClient('SoftLayer_Virtual_Guest',null, $apiUsername, $apiKey);
  $response = $client->createObject($template);

  print_r($response);

 } catch(Exception $e) {
     echo 'Cannot compute. Error is: ' . $e->getMessage();
}

?>
````

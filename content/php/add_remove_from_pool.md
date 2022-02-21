---
title: "Bandwith Pools"
description: "Adding and removing Virtual Guests and Bare Metal Servers in an exising Bandwidth Pool"
date: "2016-04-28"
classes: ["SoftLayer_Network_Bandwidth_Version1_Allotment"]
tags:
    - "bandwidthpool"
    - "bandwidth"
---

## Create Pool

```php
<?php

/* You can use the getenv() module to pull your exported Username
and API key to keep from having to store them in your files */

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');


$template = new stdClass();
$template->accountId = xxxx;
$template->bandwidthAllotmentTypeId  = 2;
$template->locationGroupId = 1;
$template->name  = 'newBWpoolPHP';

try {
  $client = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Bandwidth_Version1_Allotment',null, $apiUsername, $apiKey);
  $response = $client->createObject($template);

  print_r($response);

 } catch(Exception $e) {
     echo 'Cannot compute. Error is: ' . $e->getMessage();
}

?>
```



## Update Pool

The following script allows you to add and remove servers in an existing bandwidth pool. The script requires empty arrays when not specifying a Bare Metal or Virtual Guest Id.

```php
<?php

/* You can use the getenv() module to pull your exported Username
and API key to keep from having to store them in your files */

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');
$pool_id = 316749;

$template = new stdClass();
$template->hardwareToAdd = array();
$template->hardwareToRemove  = array();
$vm = new stdClass();
$vm->id =22983449;
$template -> cloudsToAdd[] = $vm;
$template -> cloudsToRemove = array();

try {
  $client = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Bandwidth_Version1_Allotment', $pool_id, $apiUsername, $apiKey);
  $response = $client->requestVdrContentUpdates($template);

  print_r($response);

 } catch(Exception $e) {
     echo 'Cannot compute. Error is: ' . $e->getMessage();
}

?>
```

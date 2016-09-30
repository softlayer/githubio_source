---
title: "Get primary ip address record"
description: "For a given virtual guest id, retrieve the information concerning its primary ip address"
date: "2015-01-03"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "objectMask"
    - "getObject"
---
```php
<?php

/* You can use the getenv() module to pull your exported Username
and API key to keep from having to store them in your files */

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');
$vsi_id = 22983449;

try {
  $client = \SoftLayer\SoapClient::getClient('SoftLayer_Virtual_Guest', $vsi_id, $apiUsername, $apiKey);
  $objectMask = new \SoftLayer\Common\ObjectMask();
  $objectMask->primaryNetworkComponent;
  $objectMask->primaryNetworkComponent->primaryIpAddressRecord;
  $client->setObjectMask($objectMask);
  $guest = $client->getObject();
  print_r($guest);

 } catch(Exception $e) {
     echo 'Cannot compute. Error is: ' . $e->getMessage();
}

?>
```

---
title: "Get storage credentials for Block Storage"
description: "Retrieving the username and password for Performance/Endurance Block storage"
date: "2016-08-10"
classes: ["SoftLayer_Network_Storage_Iscsi"]
tags:
    - "iscsi"
    - "blockStorage"
    - "objectMask"
---


The following script allows you retrieve the username and password for Performance/Endurance Block storage if you have authorized hosts against the storage.

```php
<?php

/* You can use the getenv() module to pull your exported Username
and API key to keep from having to store them in your files */ 

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');
$storageid = '123456';

try {
  $client = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Storage_Iscsi', $storageid, $apiUsername, $apiKey);
  $objectMask = new \SoftLayer\Common\ObjectMask();
  $objectMask->allowedHardware->allowedHost->credential;
  $objectMask->allowedVirtualGuests->allowedHost->credential;
  $client->setObjectMask($objectMask);

  $response = $client->getObject();

  print_r($response);

 } catch(Exception $e) {
     echo 'Unable to get Storage credentials: ' . $e->getMessage();
}
?>
```

---
title: "Create Storage Snapshot"
description: "Initiate a manual snapshot of an Endurance or Performance Block storage volume."
date: "2016-08-11"
classes: ["SoftLayer_Network_Storage_Iscsi"]
tags:
    - "iscsi"
    - "blockstorage"
    - "objectmask"
---

Trigger a manual snapshot creation of a Block storage volume.

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
  $response = $client->createSnapshot();

  print_r($response);

 } catch(Exception $e) {
     echo 'Unable to get Storage credentials: ' . $e->getMessage();
}
?>
```

The process can take sometime to complete. You can check the snapshots associated with a storage volume by using the code below:

```php
<?php

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');
$storageid = '123456';

try {
  $client = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Storage_Iscsi', $storageid, $apiUsername, $apiKey);
  $response = $client->getSnapshotsForVolume();

  print_r($response);

 } catch(Exception $e) {
     echo 'Unable to get Storage credentials: ' . $e->getMessage();
}
?>
```

---
title: "Create a snapshot schedule"
description: "Create a snapshot schedule for Endurance storage."
date: "2016-08-23"
classes: ["SoftLayer_Network_Storage"]
tags:
    - "enablesnapshots"
    - "blockstorage"
---

This method is not valid for Legacy iSCSI Storage Volumes. You need to have already purchased snapshot space for the script to work properly.

```php
<?php

/* You can use the getenv() module to pull your exported Username
and API key to keep from having to store them in your files */

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');
$storage_id = 11657445;

$scheduleType = 'WEEKLY';
$retentionCount = '20';
$minute = '1';
$hour = '13';
$dayOfWeek = 'SUNDAY';

try {
  $client = \SoftLayer\SoapClient::getClient('SoftLayer_Network_Storage', $storage_id, $apiUsername, $apiKey);
  $response = $client->enableSnapshots($scheduleType, $retentionCount, $minute, $hour, $dayOfWeek);

  print_r($response);

 } catch(Exception $e) {
     echo 'Cannot compute. Error is: ' . $e->getMessage();
}

?>
```

---
title: "Attach and Detach a Block Device to a Virtual_Guest"
description: "Attaching and detaching secondary block devices on Virtual Guests"
date: "2016-08-22"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "attachDiskImage"
    - "detachDiskImage"
    - "getPortableStorageVolumes"
    - "checkHostDiskAvailability"
---

Attaching a currently detached portable block device to a given guest. The disk image will need to be migrated to the host the guest is on, so make sure to check if that host has enough disk space (with checkHostDiskAvailability) before attaching. This is only required for guests with local storage guests. SAN based guests don't need that step.

Running this on a disk that is already attached will move the disk to the new guest.

```php
<?php

/* You can use the getenv() module to pull your exported Username
and API key to keep from having to store them in your files */

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');
$guest_id = 22983449;
$storage_id = 20309395;


try {
  $client = \SoftLayer\SoapClient::getClient('SoftLayer_Virtual_Guest', $guest_id, $apiUsername, $apiKey);
  $response = $client->attachDiskImage($storage_id);

  print_r($response);

 } catch(Exception $e) {
     echo 'Cannot compute. Error is: ' . $e->getMessage();
}

?>
```

To detach the disk simply change `$client->attachDiskImage($storage_id)` to `$client->detachDiskImage($storage_id)`. 

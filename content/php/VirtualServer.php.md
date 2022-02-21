---
title: "Working with Virtual Server"
description: "A few examples on interacting with Virtual Server"
date: "2020-06-11"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualguest"
---

Attaches a disk image.

Creates a transaction to attach a guest's disk image. If the disk image is already attached it will be ignored.

```php
<?php

require_once './vendor/autoload.php';

$apiUsername = "set me";
$apiKey = "set me";

$guest_id = 22983449;
$storage_id = 20309395;

$client = \SoftLayer\SoapClient::getClient('SoftLayer_Virtual_Guest', $guest_id, $apiUsername, $apiKey);
  
try {

    $response = $client->attachDiskImage($storage_id);
    print_r($response);

 } catch(Exception $e) {
    echo 'Cannot compute. Error is: ' . $e->getMessage();
}

?>
```

Get primary ip address record.

For a given virtual guest id, retrieve the information concerning its primary ip address. 

```php
<?php

require_once './vendor/autoload.php';

$apiUsername = "set me";
$apiKey = set me;

$vsi_id = 22983449;

$client = \SoftLayer\SoapClient::getClient('SoftLayer_Virtual_Guest', $vsi_id, $apiUsername, $apiKey);
    $objectMask = new \SoftLayer\Common\ObjectMask();
    $objectMask->primaryNetworkComponent;
    $objectMask->primaryNetworkComponent->primaryIpAddressRecord;
    $client->setObjectMask($objectMask);
  
try { 
    $guest = $client->getObject();
    print_r($guest);

 } catch(Exception $e) {
    echo 'Cannot get the Primary ipAddress Record: ' . $e->getMessage();
}

?>

```

Month-to-date cost of a Virtual_Guest

Determine the month-to-date cost of an hourly Virtual_Guest using getBillingItem and an objectMask. 

```php
<?php

require_once './vendor/autoload.php';

$apiUsername = 'set me';
$apiKey = 'set me';

$guest = '1234567'; # Put your VSI ID here

$client = \SoftLayer\SoapClient::getClient('SoftLayer_Virtual_Guest', $guest, $apiUsername, $apiKey);
$objectMask = new \SoftLayer\Common\ObjectMask();
$objectMask->createDate;
$objectMask->hoursUsed;
$objectMask->hourlyRecurringFee;
$objectMask->currentHourlyCharge;
$client->setObjectMask($objectMask);

try {
    $response = $client->getBillingItem();
    print_r($response)

} catch(Exception $e) {
    echo 'Cannot get the month date cost: ' . $e->getMessage();
}

?>
```

Active Private Port

It actives the private network port.

```php
<?php

require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

$apiUsername = 'set me';
$apiKey = 'set me';

$serverId = 9914387;

$client = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest', $serverId, $apiUsername, $apiKey);

try {
    $result = $client->activatePrivatePort();
    print_r($result);

} catch(Exception $e) {
    echo "Unable to activate the port: " . $e -> getMessage();
}

```

Active Public Port

It activates the public network port.

```php
<?php

require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

$apiUsername = 'set me';
$apiKey = 'set me';

$serverId = 9914387;

$client = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest', $serverId, $apiUsername, $apiKey);

try {
    $result = $client->activatePublicPort();
    print_r($result);

} catch(Exception $e) {
    echo "Unable to activate the port: " . $e -> getMessage();
}

```

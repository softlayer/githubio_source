---
title: "Get IPMI info for Bare Metal Server"
description: "Retrieve IPMI address, username, and password for all hardware on the account"
date: "2016-08-22"
classes:
  - "SoftLayer_Account"
tags:
  - "ipmi"
  - "dedicated"
  - "auth"
---

```php
<?php

require_once './vendor/autoload.php';
$apiUsername = getenv('SOFTLAYER_USERNAME');
$apiKey = getenv('SOFTLAYER_API_KEY');

$server_id = 882187;

try {
  $client = \SoftLayer\SoapClient::getClient('SoftLayer_Account', $server_id, $apiUsername, $apiKey);
  $objectMask = new \SoftLayer\Common\ObjectMask();
  $objectMask->networkManagementIpAddress;
  $objectMask->remoteManagementAccounts->username;
  $objectMask->remoteManagementAccounts->password;
  $objectMask->id;
  $objectMask->fullyQualifiedDomainName;
  $client->setObjectMask($objectMask);
  $response = $client->getHardware($objectMask);

  print_r($response);

} catch(Exception $e) {
  echo 'Cannot compute. Error is: ' . $e->getMessage();
}

?>

```

---
title: "Create a new Bandwidth Pool"
description: "This allows you to optimize your bandwidth usage by _pooling_ all of the bandwidth together for servers in a the Pool."
date: "2016-08-15"
classes: ["SoftLayer_Network_Bandwidth_Version1_Allotment"]
tags:
    - "orderTemplate"
    - "createObject"
---

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

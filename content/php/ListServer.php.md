---
title: "ListServer.php"
description: "ListServer.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
    - "SoftLayer_ObjectMask"
tags:
    - "baremetalservers"
---


```
<?php
/**
List Bare Metal servers.

This assumes the SoftLayer API PHP client
https://github.com/softlayer/softlayer-api-php-client is installed.

Important manual pages:
https://sldn.softlayer.com/reference/services/SoftLayer_Account

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
require_once('softlayer-api-php-client/SoftLayer/SoapClient.class.php');


# Your SoftLayer API username.
$username = 'set me';


# Your SoftLayer API key.
$key = 'set me';

# Connecting to the customer client for the SoftLayer_Account service
$client = SoftLayer_SoapClient::getClient('SoftLayer_Account', null, $username, $key);

/**
we will retrieve the additional information
for each server:
primaryIpAddress
primaryBackendIpAddress
datacenter
datacenterName
serviceProvider
hardwareFunctionDescription
*/
$objectMask = new SoftLayer_ObjectMask();
$objectMask->hardware->primaryIpAddress;
$objectMask->hardware->primaryBackendIpAddress;
$objectMask->hardware->datacenter;
$objectMask->hardware->datacenterName;
$objectMask->hardware->serviceProvider;
$client->setObjectMask($objectMask);

try {
       # getHardware() will get all the bare metal servers that an account has.
       $hardwareList = $client -> getHardware();
        print_r($hardwareList);
        
    } catch (Exception $e) {
        echo 'Unable to list the servers : ' . $e -> getMessage();
    }

?>

```

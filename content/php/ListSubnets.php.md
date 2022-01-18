---
title: "ListSubnets.php"
description: "ListSubnets.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
tags:
    - "subnet"
---


```php
<?php
/**
 * List Subnets.
 * It retrieves all network subnets associated with an account.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSubnets
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 */
$apiUsername = 'set me';
$apiKey = 'set me';

/**
 * Set the service to use
 */
$serviceName ='SoftLayer_Account';

/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, null, $apiUsername, $apiKey);

try {

    $receipt = $client->getSubnets();
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to get Subnet list: ' . $e->getMessage();
}

```

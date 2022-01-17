---
title: "listZones.php"
description: "listZones.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
tags:
    - "dns"
---


```php
<?php
/**
 * List Zones.
 * It retrieves the DNS domains associated with an account.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDomains
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 */
$apiUsername = 'set me';
$apiKey = 'set me';
$serviceName ='SoftLayer_Account';

/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, null, $apiUsername, $apiKey);

/**
 * get zone list through Account service.
 */
try {
    /**
     * getDomains() will get all zones that an Account contains.
     */
    $result = $client->getDomains();
    print_r($result);

} catch (Exception $e) {
    echo 'Unable to list the zones : ' . $e -> getMessage();
}

```

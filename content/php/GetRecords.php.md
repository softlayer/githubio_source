---
title: "GetRecords.php"
description: "GetRecords.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---


```
<?php
/**
 * Get Resource Records.
 * This script retrieves the individual records contained within a domain record.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 * */
$apiUsername = 'set me';
$apiKey = 'set me';
$serviceName ='SoftLayer_Dns_Domain';

/**
 * set a domain ID
 * To get Domain information: http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDomains
 */
$domainId = 1837214;

/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, $domainId, $apiUsername, $apiKey);

/**
 * Get the Resource Records through SoftLayer_Dns_Domain service.
 */
try {
    $result = $client->getResourceRecords();
    print_r($result);

} catch (Exception $e) {
    echo 'Unable to get the Resource Records: ' . $e -> getMessage();
}

```

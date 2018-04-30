---
title: "CreateZone.php"
description: "CreateZone.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---


```
<?php
/**
 * Create a Zone.
 * It creates a new domain (zone) on the SoftLayer name servers.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/createObject
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 * */
$apiUsername = 'set me';
$apiKey = 'set me';

/**
 * Set the Service to use.
 */
$serviceName ='SoftLayer_Dns_Domain';

/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, null, $apiUsername, $apiKey);

/**
 * Create an object template with configuration for new zone.
 */
$objectTemplate = new stdClass();
$objectTemplate->name = "domainname.com";
$objectTemplate->resourceRecords = array();
$objectTemplate->resourceRecords[0] = new stdClass();
$objectTemplate->resourceRecords[0]->data = "127.0.0.1";
$objectTemplate->resourceRecords[0]->host = "@";
$objectTemplate->resourceRecords[0]->type = "a";


try {
    /**
     * Creating the new zone using "createObject" method
     */
    $result = $client->createObject($objectTemplate);
    print_r($result);

} catch (Exception $e) {
    die('Failed...Unable to create a new zone: ' . $e->getMessage());
}

```

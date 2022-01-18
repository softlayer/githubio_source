---
title: "CreateRecord.php"
description: "CreateRecord.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_SoapClient"
tags:
    - "dns"
---


```php
<?php
/**
 * Create Record.
 * This script creates a new domain resource record.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObject
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
 * Set the DNS Forward Zone id that you want to add a new Record.
 */
$dnsId = 1837214;

/**
 * Set the Service to use.
 */
$serviceName ='SoftLayer_Dns_Domain_ResourceRecord';

/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, null, $apiUsername, $apiKey);


/**
 * Create an object template with configuration for new record.
 */
$objectTemplate = new stdClass();
$objectTemplate->domainId = $dnsId;
$objectTemplate->data = "127.0.0.1";
$objectTemplate->host = "@";
$objectTemplate->type = "a";

try {
    /**
     * Creating the new record using "createObject" method
     */
    $result = $client->createObject($objectTemplate);
    print_r($result);

} catch (Exception $e) {
    die('Failed...Unable to create a new Record... ' . $e->getMessage());
}

```

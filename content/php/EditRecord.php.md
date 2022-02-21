---
title: "EditRecord.php"
description: "EditRecord.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---


```php
<?php
/**
 * Edit Resource Record.
 * This script edits an existing domain resource record.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 * */
$apiUsername = 'set me';
$apiKey = 'set me';
$serviceName ='SoftLayer_Dns_Domain_ResourceRecord';

/**
 * Set a Resource Record ID
 * To get Resource Record information: http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
 */
$resourceId = 58482968;

/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, $resourceId, $apiUsername, $apiKey);

/**
 * Create an object template with new configuration of edited Resource Record.
 * TTL values:
 *          900 (15 Min)
 *          3600 (1 Hour)
 *          86400 (1 Day)
 *          604800 (1 Week)
 */
$objectTemplate = new stdClass();
$objectTemplate->data = "127.3.3.3";
$objectTemplate->host = "@";
$objectTemplate->ttl = 604800;

/**
 * Edit the Resource Records through SoftLayer_Dns_Domain_ResourceRecord service.
 */

try {
    $result = $client->editObject($objectTemplate);
    print_r($result);

} catch (Exception $e) {
    echo 'Unable to edit the current Resource Record:  ' . $e -> getMessage();
}

```

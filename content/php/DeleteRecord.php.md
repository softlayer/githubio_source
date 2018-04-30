---
title: "DeleteRecord.php"
description: "DeleteRecord.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_SoapClient"
tags:
    - "dns"
---


```
<?php
/**
 * Delete Resource Record.
 * This script deletes a domain's resource record.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObject
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
$recordId = 58478591;

/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, $recordId, $apiUsername, $apiKey);

/**
 * delete the Resource Record.
 */

try {
    $result = $client->deleteObject();
    print_r($result);

} catch (Exception $e) {
    echo 'Unable to delete the current record : ' . $e -> getMessage();
}

```

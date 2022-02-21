---
title: "ZoneDetails.php"
description: "ZoneDetails.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Dns_Domain"
    - "SoftLayer_ObjectMask"
tags:
    - "dns"
---


```php
<?php
/**
 * Zone Details
 * It retrieves the SoftLayer_Dns_Domain object whose ID number corresponds to
 * the ID number of the init parameter passed to the SoftLayer_Dns_Domain service.
 * Also, it retrieves the DNS domains associated with an account.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDomains
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getObject
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
 * Set the service to use.
 */
$serviceName ='SoftLayer_Dns_Domain';

/**
 * Sets domain's (Zone) internal identifier.
 */
$dnsId = 1846857;

/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, $dnsId, $apiUsername, $apiKey);


/**
 * Declaring an object mask to get more information about the Zone
 */
$objectMask = new SoftLayer_ObjectMask();
$objectMask->name;
$objectMask->id;
$objectMask->resourceRecords;
$client->setObjectMask($objectMask);


try {
    /**
     * Retrieving the Zone details
     */
    $result = $client->getObject();
    print_r($result);
} catch (Exception $e) {
    die('Unable to retrieve Zone information: ' . $e->getMessage());
}

```

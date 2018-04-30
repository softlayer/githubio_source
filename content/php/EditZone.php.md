---
title: "EditZone.php"
description: "EditZone.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---


```
<?php
/**
 * Edit a Zone.
 * This script edits an existing domain resource record.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
 *      http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject
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
 * Set the Zone id that you want to edit.
 */
$dnsId = 1837214;

/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, $dnsId, $apiUsername, $apiKey);

/**
 * Create a filter in order to get "resourceRecordId" to edit its values.
 */
$filter = new stdClass();
$filter->resourceRecords = new stdClass();
$filter->resourceRecords->type = new stdClass();
$filter->resourceRecords->type->operation = "soa";
$client->setObjectFilter($filter);

try {
	/**
	 * Retrieving our dns record.
	 */
    $result = new stdClass();
    $result = $client->getResourceRecords();

    $resourceRecordId = $result[0]->id;

    /**
     * Create an object template with new configuration of edited zone.
     * TTL values:
     *          900 (15 Min)
     *          3600 (1 Hour)
     *          86400 (1 Day)
     *          604800 (1 Week)
     */
    $objectTemplate = new stdClass();
    $objectTemplate->responsiblePerson = "editedContact.com";
    $objectTemplate->ttl = 900;

    /**
     * Create a client to the API service.
     */
    $clientDnsDomainResourceRecord = SoftLayer_SoapClient::getClient('SoftLayer_Dns_Domain_ResourceRecord', $resourceRecordId, $apiUsername, $apiKey);

    try{
        $editionResult = $clientDnsDomainResourceRecord->editObject($objectTemplate);
        print_r($editionResult);

    } catch(Exception $e){
        die('Unable to edit Dns Domain Resource record: ' . $e->getMessage());
    }

} catch (Exception $e) {
    die('Unable to retrieve Dns information: ' . $e->getMessage());
}

```

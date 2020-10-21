---
title: "Bandwidth"
description: "Getting bandwidth data from a server."
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_SoapClient"
tags:
    - "bandwidth"
---


## Usage

```
<?php
/**
 * Get Bandwidth usage.
 *
 * getCurrentBandwidthSummary: Retrieves an object that provides commonly used
 * bandwidth summary components for the current billing cycle.
 *
 * getBandwidthDataByDate: Use this method when needing the metric data for
 * bandwidth for a single guest. It will gather the correct input parameters
 * based on the date ranges.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getBandwidthDataByDate
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getCurrentBandwidthSummary
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 * */
$apiUsername = 'set me';
$apiKey = 'set me';
$serviceName ='SoftLayer_Virtual_Guest';

/**
 * Set the server id that you want to get bandwidth information.
 */
$serverId = 10403817;

/**
 * Create a client to the SoftLayer_Virtual_Guest API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, $serverId, $apiUsername, $apiKey);

echo "\n\n*** get Current Bandwidth Summary: ***\n";
try {

    $currentBandwidthSummary = $client->getCurrentBandwidthSummary();
    print_r($currentBandwidthSummary);
} catch (Exception $e) {
    echo 'Unable to get Current Bandwidth Summary: ' . $e->getMessage();
}

echo "\n\n*** get Bandwidth Data By Date: ***\n";
try {
    /**
     * Create an object template with required data.
     */
    $startDateTime = '08/01/2015';
    $endDateTime = '08/31/2015';
    $networkType = 'private';
    $result = $client->getBandwidthDataByDate($startDateTime, $endDateTime, $networkType);
    print_r($result);

} catch (Exception $e) {
    echo 'Unable to get the Bandwidth Data By Date: ' . $e->getMessage();
}

```

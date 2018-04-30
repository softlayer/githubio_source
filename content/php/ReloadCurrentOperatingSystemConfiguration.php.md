---
title: "ReloadCurrentOperatingSystemConfiguration.php"
description: "ReloadCurrentOperatingSystemConfiguration.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_SoapClient"
tags:
    - "virtualguest"
---


```
<?php
/**
 * Reload Current Operating System Configuration.
 * It performs an OS reload and creates a transaction to it.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/reloadCurrentOperatingSystemConfiguration
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
 * Set the server id  to reload O.S.
 */
$serverId = 7991612;

/**
 * Create a client to the SoftLayer_Virtual_Guest API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, $serverId, $apiUsername, $apiKey);

try {
    /**
     * Reloading the current O.S. Configuration.
     */
    $result = $client->reloadCurrentOperatingSystemConfiguration();
    print_r($result);

} catch(Exception $e) {
    echo "Unable to reload the current O.S. configuration: " . $e -> getMessage();
}

```

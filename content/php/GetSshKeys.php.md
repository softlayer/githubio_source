---
title: "GetSshKeys.php"
description: "GetSshKeys.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Security_Ssh_Key"
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
tags:
    - "sshkeys"
---


```
<?php
/**
 * This script retrieves customer specified SSH Keys that can be implemented onto a 
 * newly provisioned or reloaded server.
 *  
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSshKeys
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Security_Ssh_Key
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once dirname(__FILE__) . "/SoftLayer/SoapClient.class.php";

/**
 * Your SoftLayer API username
 * @var string
 */
$username = "set me";

/**
 * Your SoftLayer API key
 * Generate one at: https://control.softlayer.com/account/users
 * @var string
 */
$apiKey = "set me";

// Create a SoftLayer API client object to the "SoftLayer_Account" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey, $endpoint);

try {
	// Get Ssh Keys
    $result = $client -> getSshKeys();
	print_r($result);
    
} catch(Exception $e) {
    echo "Unable to retrieve Ssh Keys: " . $e -> getMessage();
}

```

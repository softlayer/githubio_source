---
title: "CreateSshKey.php"
description: "CreateSshKey.php"
date: "2018-04-25"
classes: 
    - "SoftLayer_Security_Ssh_Key"
    - "SoftLayer_SoapClient"
tags:
    - "sshkeys"
---


```
<?php
/**
 * This script adds ssh key to the account for use during server provisioning and os reloads
 *  
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Security_Ssh_Key/createObject
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

/**
 * Declare the parameters to create de Ssh Key
 * @var String $key - The ssh key required for create.
 * @var String $label - A descriptive name used to identify a ssh key
 * @var String $notes - A small note about a ssh key 
 */
$key = "ssh-rsa apikey_goes_hereapikey_goes_herejj0riZC4kXNafTAnMkpaFGM7BaoRgw1NyUzC585Tw2krP2OwL8KJ/fNkLn8Gt5i4NTAjIQ== rsa-key-20130612";
$label = "TestSshKey";
$notes = "This is for test";

// Build SoftLayer_Security_Ssh_Key object containing the parameters to create Ssh Key.
$templateObject = new stdClass();
$templateObject -> key = $key;
$templateObject -> label = $label;
$templateObject -> notes = $notes;

// Create a SoftLayer API client object to the "SoftLayer_Security_Ssh_Key" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Security_Ssh_Key", null, $username, $apiKey);

try {
    $result = $client -> createObject($templateObject);
	print_r($result);
    
} catch(Exception $e) {
    echo "Unable to create the Ssh Key: " . $e -> getMessage();
}

```

---
title: "DeleteSshKey.php"
description: "DeleteSshKey.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Security_Ssh_Key"
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
tags:
    - "sshkeys"
---


```php
<?php
/**
 * This script deletes a ssh key to the account. It is only necessary to specify the label, the script 
 * uses an objectFilter to get the id from Ssh Key.
 *  
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Security_Ssh_Key/deleteObject
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
 * Declare the label from Ssh Key that you wish to delete 
 * @var string
 */
$label = "TestSshKey";

// Create a SoftLayer API client object to the "SoftLayer_Account" and "SoftLayer_Security_Ssh_Key" services
$accountService = SoftLayer_SoapClient::getClient("Softlayer_Account", null, $username, $apiKey, $endpoint);
$client = SoftLayer_SoapClient::getClient("SoftLayer_Security_Ssh_Key", null, $username, $apiKey, $endpoint);

// Setting an Object Filter to get the id from the Ssh Key
$objectFilter = new stdClass();
$objectFilter -> sshKeys = new stdClass();
$objectFilter -> sshKeys -> label = new stdClass();
$objectFilter -> sshKeys -> label -> operation = "_=".$label;

$accountService -> setObjectFilter($objectFilter);

try {
    // Get the ssh key
    $resultSshKey = $accountService -> getSshKeys();
    // Set init parameter with the id from the Ssh Key that you wish to delete
    $client -> setInitParameter($resultSshKey[0] -> id);
    // Delete Ssh Key
    $result = $client -> deleteObject();
    print_r("Was the ssh key " . $label. " deleted?: " . $result);
    
} catch(Exception $e) {
    echo "Unable to delete the Ssh Key: " . $e -> getMessage();
}

```

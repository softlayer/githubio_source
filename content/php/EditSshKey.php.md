---
title: "EditSshKey.php"
description: "EditSshKey.php"
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
 * This script edits a ssh key to the account. It is only necessary to specify the label from ssh key that 
 * you wish to edit, the script uses an objectFilter to get the id from the Ssh Key.
 *  
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Security_Ssh_Key/editObject
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
 * Declare the label from Ssh Key that you wish to edit 
 * @var string
 */
$label = "TestSshKey3";

/**
 * Declare the parameters that you wish to edit for the Ssh Key.
 * @var String $label - A descriptive name used to identify a ssh key
 * @var String $notes - A small note about a ssh key 
 */
$newLabel = "TestSshKey3";
$newNotes = "This is for test3";


// Build SoftLayer_Security_Ssh_Key object containing parameters to edit the Ssh Key.
$templateObject = new stdClass();
$templateObject -> label = $newLabel;
$templateObject -> notes = $newNotes;

// Create a SoftLayer API client object to the "SoftLayer_Account" and "SoftLayer_Security_Ssh_Key" services
$accountService = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey, $endpoint);
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
    $result = $client -> editObject($templateObject);
    print_r("Was the ssh key " . $label. " edited?: " . $result);
    
} catch(Exception $e) {
    echo "Unable to edit the Ssh Key: " . $e -> getMessage();
}

```

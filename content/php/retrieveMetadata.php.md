---
title: "retrieveMetadata.php"
description: "retrieveMetadata.php"
date: "2018-04-25"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "metadata"
---


```php
<?php

/**
 * Retrieves the user data for the VSIs in the account
 * 
 * The script gets the user metadata for a VSI in the account we make a simple
 * call th the getVirtualGuests() in the SoftLayer_Virtual_Guest API service
 * and we set an object mask to get the information about the user data
 * 
 * Manual pages
 * see http://sldn.softlayer.com/reference/services/SoftLayer_Account
 * see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
 * license <http://sldn.softlayer.com/article/License>
 * author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('C:/scripst/getdetails/SoftLayer/SoapClient.class.php');

/**
 * Your SoftLayer API username and key.
 *
 * Generate an API key at the SoftLayer Customer Portal:
 * https://manage.softlayer.com/Administrative/apiKeychain
 */
$apiUsername = '';
$apiKey = 'apikey_goes_here';

$client = Softlayer_SoapClient::getClient('SoftLayer_Account', null, $apiUsername, $apiKey);

# Add the object mask to the call to get the information about the user data.
$client->setObjectMask("mask[userData]");

try {
    # Retrieve our account's VSIs records.
    $result = $client->getVirtualGuests();
    print_r($result);
} catch (Exception $e) {
    die('Unable to retrieve the VSI list. ' . $e->getMessage());
}

?>
```

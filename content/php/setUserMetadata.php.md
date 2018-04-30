---
title: "setUserMetadata.php"
description: "setUserMetadata.php"
date: "2018-04-25"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "metadata"
---


```
<?php

/**
 * Set the user data for a VSI.
 * 
 * The script sets the user metadata for a VSI we make a simple
 * call th the setUserMetadata() in the SoftLayer_Virtual_Guest API service
 *
 * Manual pages
 * see http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
 * see http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setUserMetadata
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

$virtualGuestService = Softlayer_SoapClient::getClient('SoftLayer_Virtual_Guest', null, $apiUsername, $apiKey);

// The user data you wish to set
$userData = ["this is my user data"];

// The id of the VSI where you want to set the user data
$virtualGuestId = 7370502;

// Setting the init parameter in the service
$virtualGuestService->setInitParameter($virtualGuestId);

try {
    // Setting the user metadata.
    $result = $virtualGuestService->setUserMetadata($userData);
    print_r($result);
} catch (Exception $e) {
    die('Unable to set the user metadata. ' . $e->getMessage());
}

?>
```

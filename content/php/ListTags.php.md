---
title: "ListTags.php"
description: "ListTags.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "tag"
---


```
<?php
/**
 * List the tags for a VSI
 * 
 * The scripts list all the tags set in an arbitrary  VSI,
 * it uses the SoftLayer_Virtual_Guest::getTagReferences method
 * to get the tags. For more information please see below
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getTagReferences
 * 
 * License: http://sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('Softlayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

$virtualGuestService = Softlayer_SoapClient::getClient('SoftLayer_Virtual_Guest', null, $apiUsername, $apiKey);

// The Id of the VSI you wish to list the tags
$virtualGuestId = 7844984;
$virtualGuestService->setInitParameter($virtualGuestId);

try {
    // Send the request to list the tags
    $result = $virtualGuestService->getTagReferences();
    print_r($result);

} catch (Exception $e) {
    echo 'Unable to list the tags : ' . $e -> getMessage();
}


?>

```

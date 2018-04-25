---
title: "SetTags.php"
description: "SetTags.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "tag"
---


```
<?php
/**
 * Set tags for a VSI
 * 
 * The script sets the tags for an arbitrary VSI,
 * it makes a single call to the SoftLayer_Virtual_Guest::setTags method
 * For more information please see below.
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setTags
 * 
 * License: http://sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('Softlayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

$virtualGuestService = Softlayer_SoapClient::getClient('SoftLayer_Virtual_Guest', null, $apiUsername, $apiKey);

// The id of the VSI to set the tags
$virtualGuestId = 7844984;
$virtualGuestService->setInitParameter($virtualGuestId);

// The tags you wish to set in the VSI
$tags = "mytag1, mytag2, mytag3";

// Sending the request to set the tags
$result = $virtualGuestService->setTags($tags);
print_r($result);

?>

```

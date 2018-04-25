---
title: "GetNetworkMonitors.php"
description: "GetNetworkMonitors.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_SoapClient"
tags:
    - "monitoring"
---


```
<?php
/**
 * Example to get the network monitors in a VSI
 * 
 * The script calls the SoftLayer_Virtual_Guest::getObject method
 * and uses a mask to get the information of the network monitors
 * in the VSI.
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject
 * http://sldn.softlayer.com/article/Object-Masks
 * 
 * License <http://sldn.softlayer.com/article/License>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * 
 */
require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API key and username.
$apiUsername = 'set me';
$apiKey = 'set me';

# The if of the vsi you wish to get the network monitors
$vsiId = 7322908;

# Declaring our API client 
$virtualGuestService = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest', $vsiId, $apiUsername, $apiKey);

# Defining an object mask in order to get the information related
# to the network monitors and network components.
$objectMask = 'mask[networkMonitors,networkMonitorCount,networkComponentCount,networkComponents]';

try {
    $virtualGuestService->setObjectMask($objectMask);
    print_r($virtualGuestService->getObject());
} catch (Exception $e) {
    echo 'Unable to get the monitors: ' . $e->getMessage();
}

```

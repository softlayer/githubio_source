---
title: "GetSubnets.php"
description: "GetSubnets.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlan"
---


```
<?php
/**
 * Retrieve the subnets for a VLAN
 * 
 * Retrieve all the subnets for a determinate VLAN
 * associated with a SoftLayer customer account
 * We do this with a call to the getSubnets() method in the
 * SoftLayer_Network_Vlan API service. See below for more details.
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getSubnets
 * 
 * License: http://sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('SoftLayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

// The VLAN id you wish to see its subnets
$vlanId = 557984;

// Declaring the API client
$networkVlanService = Softlayer_SoapClient::getClient('SoftLayer_Network_Vlan', null, $apiUsername, $apiKey);

$networkVlanService->setInitParameter($vlanId);

// Sending the request to get the subnets
try {
    $result = $networkVlanService->getSubnets();
    print_r($result);
} catch (Exception $e) {
    die('Unable to retrieve the subnets. ' . $e->getMessage());
}

```

---
title: "SwitchPortStats.php"
description: "SwitchPortStats.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_NetworkComponent"
    - "SoftLayer_Container_Network_Port_Statistic"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Network_Component"
tags:
    - "vlan"
---


```
<?php
/**
 * Retrieve a list of switch port statistics for a server's network interfaces.
 * 
 * This script makes a single call to the getPortStatistics() method in the
 * SoftLayer_Network_Component API service
 * for each of a server's network components to query port statistics for that
 * interface from SoftLayer's switches. Port statistics are modeled by the
 * SoftLayer__Container_Network_Port_Statistic data type
 * See below for more details.
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_NetworkComponent/getPortStatistics
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Network_Port_Statistic
 * 
 * License: http://sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('SoftLayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

# Your server's id. Call the getHardware() method in the SoftLayer_Account API
# service (http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware)
# to get a list of your account's hardware records.
$serverId = 87165;

// Declaring the API client
$hardwareServerService = Softlayer_SoapClient::getClient('SoftLayer_Hardware_Server', null, $apiUsername, $apiKey);
$networkComponentService = Softlayer_SoapClient::getClient('SoftLayer_Network_Component', null, $apiUsername, $apiKey);

# Switchport statistics are measured off the server's network components. Use
# an object mask to network component records along with our server record.
$objectMask = new SoftLayer_ObjectMask();
$objectMask->networkComponents;
$hardwareServerService->setObjectMask($objectMask);

$hardwareServerService->setInitParameter($serverId);

try {
    # Making the call to retrieve our hardware record. Once we have that we can query
    # the server's network components.
    $server = $hardwareServerService->getObject();
} catch (Exception $e) {
    die('Unable to retrieve server record. ' . $e->getMessage());
}

# Separating our network components for easier processing later.
$networkComponents = $server->{'networkComponents'};
print ("Switchport statistics for " . $server->{'fullyQualifiedDomainName'});

# Loop through our server's network components. For each NIC make a call to the
# SoftLayer_Network_Component API service method getPortStatics() to get a list
# of switchport statistics retrieved from the switch on the other side of your
# NIC. Print a simple report per NIC.
foreach  ($networkComponents as &$networkComponent) {
    # Skipping the management network component.
    if ($networkComponent->{'name'} != 'mgmt'){
        try {
            # Retrieving switchport statistics for the NIC.
            $networkComponentService->setInitParameter($networkComponent->{'id'});
            $stats = $networkComponentService->getPortStatistics();
            print_r ($stats);
        } catch (Exception $e) {
            die('Unable to retrieve switchport statics for . ' . $e->getMessage());
        }
    }
}

```

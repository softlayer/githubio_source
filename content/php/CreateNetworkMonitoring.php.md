---
title: "CreateNetworkMonitoring.php"
description: "CreateNetworkMonitoring.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```
<?php
/**
 * Example to create a network monitoring
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/createObject
 * 
 * License <http://sldn.softlayer.com/article/License>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * 
 */
require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

# The Id of the server you wish to monitor
$serverId = 7377448;

# Id of the query type which can be found with SoftLayer_Network_Monitor_Version1_Query_Host_Stratum/getAllQueryTypes.
# This example uses SERVICE PING: Test ping to address, will not fail on slow server response due to high latency or
# high server load
$queryTypeId = 1;

# IP address on the previously defined server to monitor
$ipAddress = '10.120.63.196';

$userCustomerNotificiation = Softlayer_SoapClient::getClient('SoftLayer_Network_Monitor_Version1_Query_Host', null, $apiUsername, $apiKey);

# Define the SoftLayer_Network_Monitor_Version1_Query_Host templateObject.
# the template object will create a monitoring network for a virtual guest
# to create the  the monitoring network in a hardware change "guestId" by "hardwareId"
$newMonitor = new stdClass();
$newMonitor->guestId = $serverId;
$newMonitor->queryTypeId = $queryTypeId;
$newMonitor->ipAddress = $ipAddress;


try {
    $result = $userCustomerNotificiation->createObject($newMonitor);
    print_r($result);
} catch (Exception $e) {
    echo 'Unable to create the network monitoring: ' . $e->getMessage();
}

?>

```

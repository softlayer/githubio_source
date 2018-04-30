---
title: "DeleteNetworkMonitoring.php"
description: "DeleteNetworkMonitoring.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```
<?php
/**
 * Example to delete network monitoring
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/deleteObject
 *
 * License <http://sldn.softlayer.com/article/License>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

# The Id of the network monitoring you wish to delete
$monitoringDeleteId = 1789133;

$userCustomerNotificiation = Softlayer_SoapClient::getClient('SoftLayer_Network_Monitor_Version1_Query_Host', null, $apiUsername, $apiKey);
$userCustomerNotificiation->setInitParameter($monitoringDeleteId);

try {
    # Sending the request to delete the object
    $result = $userCustomerNotificiation->deleteObject();
    print_r($result);
} catch (Exception $e) {
    echo 'Unable to delete the network monitoring: ' . $e->getMessage();
}

?>

```

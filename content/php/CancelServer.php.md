---
title: "CancelServer.php"
description: "CancelServer.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Item_Hardware"
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
<?php
# Cancel servers from a list of IPs
#
# This script looks for a server with a determinate IP address and delete it.
#
# It makes a single call to the cancelService() method in the
# SoftLayer_Billing_Item API service
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item_Hardware
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require_once('softlayer-api-php-client/SoftLayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

# the list of IPs from the servers you wish cancel
$ipsToCancel = array('1.1.1.1', '2.2.2.2');

# Declare a new API service object for the
# SoftLayer_Hardware_Server API service
# SoftLayer_Billing_Item service
$hardwareServerService = SoftLayer_SoapClient::getClient('SoftLayer_Hardware_Server', null, $username, $key);
$billingItemService = SoftLayer_SoapClient::getClient('SoftLayer_Billing_Item', null, $username, $key);

# Add an object mask to retrieve our billing items related to the servers
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# for a list of the relational properties you can retrieve along with hardware.
$object_mask = 'mask[billingItem]';

# Make the call to retrieve our hardware records along with their billing item.
# Setting the init parameter with the server ID
$hardwareServerService->setObjectMask($object_mask);

try {
    foreach ($ipsToCancel as $ipToCancel)
    {
        $server = $hardwareServerService->findByIpAddress($ipToCancel);
        $billingId = $server->{'billingItem'}->{'id'};
        $billingItemService->setInitParameter($billingId);
        $result = $billingItemService->cancelItem(false, false, "No longer needed", "Api test");
        var_dump($result);
    }
} catch(Exception $e) {
    echo "Unable to cancel the server: " . $e -> getMessage();
}
?>

```

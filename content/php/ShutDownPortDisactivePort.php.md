---
title: "ShutDownPortDisactivePort.php"
description: "ShutDownPortDisactivePort.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```php
<?php
# Sets the networks speed for a hardware devices
#
# This script makes a single call to the setPublicNetworkInterfaceSpeed() method
# to change the speed to public network or call the setPrivateNetworkInterfaceSpeed method
# to change the speed to private network.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/setPublicNetworkInterfaceSpeed
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/setPrivateNetworkInterfaceSpeed
#
# See below for more details.
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require_once('softlayer-api-php-client/SoftLayer/SoapClient.class.php');

# Your SoftLayer API username.
$username = 'set me';

# Your SoftLayer API key.
$key = 'set me';

# The ID of the hardware you wish modified the networks.
$hardwareID = 167407;

# The speed you wish configure if you want to disconnect the network you should set the value to '0'
$newSpeedPublicNetwork = 10;
$newSpeedPrivateNetwork = 100;

# Connecting to the customer client for the SoftLayer_Hardware_Server service
$hardwareServerService = SoftLayer_SoapClient::getClient('SoftLayer_Hardware_Server', null, $username, $key);
# Setting the init parameter for our service
$hardwareServerService->setInitParameter($hardwareID);

try {
    # It is not possible to update the two networks at same time, you need to update one and wait until
    # the transaction is completed to update the second one.
    $result = $hardwareServerService->setPublicNetworkInterfaceSpeed($newSpeedPublicNetwork);
    print ("The public network speed has been modified? " . $result);
    $result = $hardwareServerService->setPrivateNetworkInterfaceSpeed($newSpeedPrivateNetwork);
    print ("The private network speed has been modified? " . $result);
} catch (Exception $e) {
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    echo 'Unable to modify networks. :' . $e -> getMessage();
}
?>

```

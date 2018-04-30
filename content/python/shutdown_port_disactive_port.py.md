---
title: "shutdown_port_disactive_port.py"
description: "shutdown_port_disactive_port.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Sets the networks speed for a hardware devices

This script makes a single call to the setPublicNetworkInterfaceSpeed() method
to change the speed to public network or call the setPrivateNetworkInterfaceSpeed method
to change the speed to private network.

See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/setPublicNetworkInterfaceSpeed
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/setPrivateNetworkInterfaceSpeed

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

# The ID of the hardware you wish modified the networks.
hardwareId = 308926

# The speed you wish configure if you want to disconnect the network you should set the value to '0'
newSpeedPublicNetwork = 0
newSpeedPrivateNetwork = 10

# Declaring the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
hardwareServerService = client['SoftLayer_Hardware_Server']

try:
    """
    It is not possible to update the two networks at same time, you need to update one and wait until
    the transaction is completed to update the second one, interchange the methods below commenting which
    type of interface it's NOT required to modify.
    """
    result = hardwareServerService.setPublicNetworkInterfaceSpeed(newSpeedPublicNetwork, id=hardwareId)
    print("The public network speed has been modified? " + str(result))
    # result = hardwareServerService.setPrivateNetworkInterfaceSpeed(newSpeedPrivateNetwork, id=hardwareId)
    # print("The private network speed has been modified? " + str(result))
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to modify networks: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

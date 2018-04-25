---
title: "edit_private_port_speed.py"
description: "edit_private_port_speed.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```
"""
Change Private Network Interface Speed.
It sets the private network interface speed to the new speed.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setPrivateNetworkInterfaceSpeed

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

virtualGuestId = 35747489
newSpeed = 100

# Create a SoftLayer Client.
client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

# Changing the private port speed
try:
    result = client['Virtual_Guest'].setPublicNetworkInterfaceSpeed(newSpeed,
            id=virtualGuestId)
    pp(result)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to set the new private port speed value faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```

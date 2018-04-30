---
title: "activate_public_port.py"
description: "activate_public_port.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```
"""
Activate Public Port.
It Activate the public network port


Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/activatePublicPort

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

# Set the server id in order to activate the network port.
serverId = 35747489

# Set up your API client
client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    # The expected result after executing the script is: true
    result = client['Virtual_Guest'].activatePublicPort(id=serverId)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to activate the public port faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```

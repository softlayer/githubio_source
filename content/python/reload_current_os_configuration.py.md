---
title: "reload_current_os_configuration.py"
description: "reload_current_os_configuration.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```
"""
Reload current operating system configuration.
It creates a transaction to perform an OS reload

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/reloadCurrentOperatingSystemConfiguration

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

# Set the server id that you wish to reload.
serverId = 35747489

# Create a SoftLayer Client.
client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

# Reload the Virtual Guest
try:
    # Make the call to reload the server.
    result = client['Virtual_Guest'].reloadCurrentOperatingSystemConfiguration(
        id=serverId)
    pp(result)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to reload the server faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```

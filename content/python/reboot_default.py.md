---
title: "reboot_default.py"
description: "reboot_default.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "virtualserver"
---


```
"""
Reboot Virtual Guest.
It reboots a SoftLayer Virtual Guest


Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/rebootDefault

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer

# From pprint import pprint as pp
# For nice debug output
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# If you don't know your server id you can call getVirtualGuests() in the
# SoftLayer_Account API service to get a list of Virtual Guests
serverId = 35747489

# Create a connection to API service.
client = SoftLayer.create_client_from_env(
        username=API_USERNAME,
        api_key=API_KEY
)

# Reboot the Virtual Guest
try:

    result = client['Virtual_Guest'].rebootDefault(id=serverId)
    pp(result)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to reboot the server faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```

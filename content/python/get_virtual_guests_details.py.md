---
title: "get_virtual_guests_details.py"
description: "get_virtual_guests_details.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "virtualserver"
---


```
"""
Get Virtual Guest details. It retrieves virtual guest information.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer

# For nice debug output:
from pprint import pprint as pp

# Set your SoftLayer API username and key.

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# Set the server id that you wish to get details.
# Call the getVirtualGuests method from SoftLayer_Account
serverId = 35747489

# Retrieve the wanted server information using a mask
mask = 'operatingSystem.passwords, networkComponents, datacenter, notes'

# Make a connection to the Virtual_Guest service.
client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    # Make the call to retrieve the server details.
    virtualGuestDetails = client['Virtual_Guest'].getObject(id=serverId,
                                                    mask=mask)
    pp(virtualGuestDetails)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get the Virtual Guest infomrmation faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```

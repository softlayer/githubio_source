---
title: "get_virtual_guests_list.py"
description: "get_virtual_guests_list.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "virtualserver"
---


```
"""
List Virtual Guests.

Retrieve an account's associated virtual guest objects'

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
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

# Creates an object filter to get virtual guests with host different of zero.
filterInstance = {
    'virtualGuests': {
        'host': {
            'operation': 'not null'
        }
    }
}

# Creates a new connection to the API service.
client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    # Listing the Virtual Guests for current Account.
    listInstances = client['Account'].getVirtualGuests(
        limit=100, offset=0,
        filter=filterInstance)  # Page 1
    pp(listInstances)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get the Virtual Guests list faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```

---
title: "get_virtual_server_notes.py"
description: "get_virtual_server_notes.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```
"""
Get notes from a VSI.

The script retrieves the notes for an arbitrary VSI, it makes a single call
to  SoftLayer_Virtual_Guest::getObject method.
for more information see below:

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject/
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

#Declare variables
virtualGuestId = 35747489

# Declare the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
virtualServer = client['SoftLayer_Virtual_Guest']

try:
    result = virtualServer.getObject(id=virtualGuestId)
    print (result['notes'])
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to get the notes. "
          % (e.faultCode, e.faultString))

```

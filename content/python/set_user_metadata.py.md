---
title: "set_user_metadata.py"
description: "set_user_metadata.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "metadata"
---


```
"""
Set the user data for a VSI.

The script sets the user metadata for a VSI we make a simple
call the setUserMetadata() in the SoftLayer_Virtual_Guest API service

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setUserMetadata

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

"""
Client configuration
Your SoftLayer API username and key.
"""

USERNAME = 'set me'
API_KEY = 'set me'

# The user data you wish to set
userData = ["this is my user data 2"]

# The id of the VSI where you want to set the user data
virtualGuestId = 7370502

# Declaring the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
virtualGuestService = client['SoftLayer_Virtual_Guest']

try:
    # Setting the user metadata
    result = virtualGuestService.setUserMetadata(userData, id=virtualGuestId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to set the tags faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```

---
title: "retrieve_metadata.py"
description: "retrieve_metadata.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "metadata"
---


```
"""
Retrieves the user data for the VSIs in the account

The script gets the user metadata for a VSI in the account we make a simple
call the getVirtualGuests() in the SoftLayer_Virtual_Guest API service
and we set an object mask to get the information about the user data

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests

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

# Declaring the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

# Adding the object mask to the call to get the information about the user data.
objectMask = "mask[userData]"

try:
    # Retrieving our account's VSI records.
    result = accountService.getVirtualGuests(mask=objectMask)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the tags faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```

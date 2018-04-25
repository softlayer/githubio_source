---
title: "allow_access_from_virtual_guest.py"
description: "allow_access_from_virtual_guest.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Storage"
tags:
    - "iscsi"
---


```
"""
Allow access to Consistent Performance Storage iSCSI.
This script allows the access to Consistent Performance Storage iSCSI from a virtual guest using the
SoftLayer_Network_Storage::allowAccessFromVirtualGuest method.
See below references for more details.
Important manual Pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage/allowAccessFromVirtualGuest
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer

# For nice debug output:
import pprint

# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'

"""
Set the storage Id to allow the access from a virtual instance, you can get
a list of storage with SoftLayer::getNetworkStorage
"""
storageId = 4379484
"""
Set the server id which will be attached to the storage, retrieve a list of
virtual guests by SoftLayer_Account::getVirtualGuests
"""
serverId = 7598482

virtualGuestTemplate = {'id': serverId}

# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
try:
    result = client['SoftLayer_Network_Storage'].allowAccessFromVirtualGuest(virtualGuestTemplate, id=storageId)
    print("Allowed access to storage")
    pprint.pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Error cannot attach the server  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```

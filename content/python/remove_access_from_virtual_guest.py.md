---
title: "remove_access_from_virtual_guest.py"
description: "remove_access_from_virtual_guest.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Storage"
tags:
    - "iscsi"
---


```
"""
Remove access to Consistent Performance Storage iSCSI.

This script removes the access to Consistent Performance Storage iSCSI from a virtual guest by calling to
SoftLayer_Network_Storage::removeAccessFromVirtualGuest method.

See below references for more details.
Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage/removeAccessFromVirtualGuest
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

# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
"""
Set the storage Id to remove the access from a virtual instance, you can get
a list of storage with SoftLayer::getNetworkStorage
"""
storageId = 4379484
"""
Set the server id which will be detached from the storage, retrieve a list of
virtual guests by SoftLayer_Account::getVirtualGuests
"""
serverId = 7598482
virtualGuestTemplate = {'id': serverId}
try:
    result = client['SoftLayer_Network_Storage'].removeAccessFromVirtualGuest(virtualGuestTemplate, id=storageId)
    print("Access removed  to storage")
    pprint.pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Error cannot remove access  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```

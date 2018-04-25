---
title: "get_snapshot_space_available.py"
description: "get_snapshot_space_available.py"
date: "2018-04-25"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Storage"
tags:
    - "networkstorage"
---


```
"""
Get snapshot space available

The script makes a single call to SoftLayer_Account::getNetworkStorage
method to get the network storages into the account and uses a mask
in order to get the snapshot space available.

See below for more details

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkStorage
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Storage

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

"""
Your SoftLayer API username and key.

Generate an API key at the SoftLayer Customer Portal:
https://manage.softlayer.com/Administrative/apiKeychain
"""
USERNAME = ''
API_KEY = 'apikey_goes_here'

# Declare a new API service object
client = SoftLayer.Client(username=USERNAME,api_key=API_KEY)
accountService = client['Account']

# Setting the object mask to get the snapshot space available value.
storageMask = "id, capacityGb, username, snapshotSpaceAvailable, vendorName"

try:
    storageUnits = accountService.getNetworkStorage(mask=storageMask)
    print (storageUnits)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to retrieve the bare metal list. "
          % (e.faultCode, e.faultString))



```

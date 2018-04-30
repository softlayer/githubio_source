---
title: "get_unattached_portable_storages.py"
description: "get_unattached_portable_storages.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_Disk_Image"
tags:
    - "portablestorage"
---


```
"""
Get unattached portal storages.

The script gets all the unattached portal storages in the account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getPortableStorageVolumes
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Disk_Image
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

# Declaring a object mask to get information about the guest
# of the portal storage.
objeckMask = "mask[storageRepository[guests]]"

unattachedPortalStorages = []

# Looking for the portal storages which do not have any guest.
try:
    portableStorages = accountService.getPortableStorageVolumes(mask=objeckMask)
    for storage in portableStorages:
        if 'storageRepository' in storage:
            if len(storage['storageRepository']['guests']) == 0:
                unattachedPortalStorages.append(storage)
    print(unattachedPortalStorages)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the portable storage list. "
          % (e.faultCode, e.faultString))

```

---
title: "Get storage credentials for Block Storage"
description: "Retrieving the username and password for Performance/Endurance Block storage"
date: "2016-04-28"
classes: ["SoftLayer_Network_Storage_Iscsi"]
tags:
    - "Iscsi"
    - "BlockStorage"
---

The following script allows you retrieve the username and password for Performance/Endurance Block storage if you have authorized hosts against the storage.

```python
"""
Get credentials for a authorized hosts of a SoftLayer_Network_Storage_Iscsi 

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage_Iscsi
"""

import SoftLayer
import json

iscsiStorageId = 1234567

client = SoftLayer.create_client_from_env()
networkStorageIscsiService = client['SoftLayer_Network_Storage_Iscsi']

objectMask = 'mask[allowedHardware[allowedHost[credential]],allowedVirtualGuests[allowedHost[credential]]]'

try:
    iscsiStorage = networkStorageIscsiService.getObject(mask=objectMask, id=iscsiStorageId)
    print(json.dumps(iscsiStorage, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the Network Storage Iscsi. faultCode=%s, faultString=%s"
        % (e.faultCode, e.faultString))

```

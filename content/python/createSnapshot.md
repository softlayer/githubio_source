---
title: "Create Storage Snapshot"
description: "Initiate a manual snapshot of an Endurance or Performance Block storage volume."
date: "2016-08-11"
classes: ["SoftLayer_Network_Storage_Iscsi"]
tags:
    - "iscsi"
    - "blockStorage"
    - "objectMask"
    - "storage"
---

Trigger a manual snapshot creation of a Block storage volume.

```python
import SoftLayer
import json

iscsiStorageId = 8744521

client = SoftLayer.create_client_from_env()
networkStorageIscsiService = client['SoftLayer_Network_Storage_Iscsi']

try:
    iscsiStorage = networkStorageIscsiService.createSnapshot(id=iscsiStorageId)
    print(json.dumps(iscsiStorage, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the Network Storage Iscsi. faultCode=%s, faultString=%s"
        % (e.faultCode, e.faultString))
```

The process can take sometime to complete. You can check the snapshots associated with a storage volume by using the code below:

```python
import SoftLayer
import json

iscsiStorageId = 8744521

client = SoftLayer.create_client_from_env()
networkStorageIscsiService = client['SoftLayer_Network_Storage_Iscsi']

try:
    iscsiStorage = networkStorageIscsiService.getSnapshotsForVolume(id=iscsiStorageId)
    print(json.dumps(iscsiStorage, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the Network Storage Iscsi. faultCode=%s, faultString=%s"
        % (e.faultCode, e.faultString))
```

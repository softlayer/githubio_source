---
title: "Manage Block/File storages with python-managers"
description: "It shows how to authorize, deauthorize, order replicant volume, etc."
date: "2018-11-21"
classes: 
    - "SoftLayer_Network_Storage"    
tags:
    - "block"    
    - "file"
    - "endurance"
    - "performance"
---
[Block Storage Manager](https://softlayer-python.readthedocs.io/en/latest/api/managers/block.html) and [File Storage Manager](https://softlayer-python.readthedocs.io/en/latest/api/managers/file.html) provide several methods which can be used to manage the file/block storage devides, following are some examples which can be used for block or file storage devices, just instantiate `FileStorageManager` instead of `BlockStorageManager` if you want to work whit this kind of storages:

```python
client = SoftLayer.Client()
mgr = SoftLayer.FileStorageManager(client)

```

**Auhorize Hosts**

```python
import SoftLayer
from pprint import pprint

client = SoftLayer.Client()
mgr = SoftLayer.BlockStorageManager(client)

# Storage, hardware, and virtual guest must have in the same location
storage_id = 19026105
hwd_ids = [1427759,1580803]
vs_ids = [55265213,55282263]

try:
    result = mgr.authorize_host_to_volume(storage_id,
                                          hardware_ids=hwd_ids,
                                          virtual_guest_ids=vs_ids)
    pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    pprint('Unable to authorize hosts. %s, %s ' % (e.faultCode, e.faultString))
```

**Get list of authorized hosts**

```py
import SoftLayer
from pprint import pprint

client = SoftLayer.Client()
mgr = SoftLayer.BlockStorageManager(client)

storage_id = 19026105
object_mask = 'mask[allowedHardware[id,hostname,domain,primaryBackendIpAddress],'\
              'allowedVirtualGuests[id,hostname,domain,primaryBackendIpAddress],'\
              'allowedIpAddresses,allowedSubnets,id]'
try:
    result = mgr.get_block_volume_access_list(storage_id, mask=object_mask)
    pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    pprint('Unable to authorize hosts. %s, %s ' % (e.faultCode, e.faultString))
```

Use the method `get_file_volume_access_list` instead of `get_block_volume_access_list` if you have been instantiate the `FileStorageManager` class

```python
result = mgr.get_file_volume_access_list(storage_id, mask=object_mask)

```

**Deauhorize Hosts**

```python
import SoftLayer
from pprint import pprint

client = SoftLayer.Client()
mgr = SoftLayer.BlockStorageManager(client)

storage_id = 19026105
hwd_ids = [1427759,1580803]
vs_ids = [55265213,55282263]

try:
    result = mgr.deauthorize_host_to_volume(storage_id,
                                            hardware_ids=hwd_ids,
                                            virtual_guest_ids=vs_ids)
except SoftLayer.SoftLayerAPIError as e:
    pprint('Unable to deauthorize hosts. %s, %s ' % (e.faultCode, e.faultString))
```

**Order a replicant volume**

```py
import SoftLayer
from pprint import pprint

client = SoftLayer.Client()
mgr = SoftLayer.BlockStorageManager(client)

storage_id = 19026105
schedule = 'WEEKLY'         # values: HOURLY, DAILY, WEEKLY
location = 'dal12'

try:
    result = mgr.order_replicant_volume(storage_id, schedule, location)
    pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    pprint('Unable to create replica. %s, %s ' % (e.faultCode, e.faultString))
```

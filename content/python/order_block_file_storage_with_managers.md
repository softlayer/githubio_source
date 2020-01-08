---
title: "Order Block/File Storages with Managers"
description: "Creates the new STaaS volumenes, they can be performance/endurance file or block devices"
date: "2018-11-20"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Storage_AsAService"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Network_Storage"
tags:
    - "order"
    - "block"
    - "file"
    - "endurance"
    - "performance"
---

**Order a Block Storage**

The [Block Storage Manager](https://softlayer-python.readthedocs.io/en/latest/api/managers/block/) class provides different methods which can be used to order, cancel, list, etc., block storage devices, the following example shows how to order an endurance storage in an easy way and it can also be modified to order a performance type.

```python
import SoftLayer
from pprint import pprint

client = SoftLayer.Client()
block_mgr = SoftLayer.BlockStorageManager(client)

storage_type = 'endurance'  # Set 'performance' if you want this kind of storage
location = 'dal10'
hourly = True
size = 20           # Storage size (GB), minimum = 20 and maximum = 12000.
iops = 2            # Tier Level IOPS for endurance can be: 0.25, 2, 4 or 10, and
                    # for performance storage it can be between 100 - 1000 IOPS.
snapshot_size = 5   # Snapshot can be 0, 5, 10, 20
os_type = 'LINUX'   # values: HYPER_V, LINUX, VMWARE, WINDOWS_2008, WINDOWS_GPT, WINDOWS, XEN

try:
    # Set iops instead of tier_level argument for performance block storages.
    result = block_mgr.order_block_volume(storage_type, location, size, os_type,
                                          tier_level=iops,snapshot_size=snapshot_size,
                                          hourly_billing_flag=hourly)

    pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    pprint('Unable to create the Storage. %s, %s ' % (e.faultCode, e.faultString))
```

**Order a File Storage**

In the same way than block storage, the [File Storage Manager](https://softlayer-python.readthedocs.io/en/latest/api/managers/file/) class can be used to order, cancel, list, etc., file storage devices, the following example order a performance storage.
```python
import SoftLayer
from pprint import pprint

client = SoftLayer.Client()
file_mgr = SoftLayer.FileStorageManager(client)

storage_type = 'performance'  # Set 'endurance' if you want this kind of storage
location = 'dal10'
hourly = True
size = 20           # Storage size (GB), minimum = 20 and maximum = 12000.
iops = 100          # IOPS for performance storage can be between 100 - 1000 IOPS, and
                    # tier Level IOPS for endurance can be: 0.25, 2, 4 or 10.
snapshot_size = 5   # Snapshot can be 0, 5, 10, 20

try:
    # Set tier_level instead of iops argument for endurance file storage.
    result = file_mgr.order_file_volume(storage_type, location, size, iops=iops,
                                        snapshot_size=snapshot_size, hourly_billing_flag=hourly)

    pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    pprint('Unable to create the storage. %s, %s ' % (e.faultCode, e.faultString))

```

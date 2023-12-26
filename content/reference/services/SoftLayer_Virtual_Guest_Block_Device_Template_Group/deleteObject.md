---
title: "deleteObject"
description: "Deleting a block device template group is different from the deletion of other objects.  A block device template group can contain several gigabytes of data in its disk images.  This may take some time to delete and requires a transaction to be created.  This method creates a transaction that will delete all resources associated with the block device template group. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Block_Device_Template_Group/{SoftLayer_Virtual_Guest_Block_Device_Template_GroupID}/deleteObject'
```

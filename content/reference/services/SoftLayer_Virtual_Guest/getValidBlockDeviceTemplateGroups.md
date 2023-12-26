---
title: "getValidBlockDeviceTemplateGroups"
description: "This method will return the list of block device template groups that are valid to the host. For instance, it will validate that the template groups returned are compatible with the size and number of disks on the host. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getValidBlockDeviceTemplateGroups'
```

---
title: "checkHostDiskAvailability"
description: "Checks the associated host for available disk space to determine if guest migration is necessary. This method is only used with local disks. If this method returns false, calling attachDiskImage($imageId) will automatically migrate the destination guest to a new host before attaching the portable volume. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/checkHostDiskAvailability'
```

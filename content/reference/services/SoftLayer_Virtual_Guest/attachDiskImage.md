---
title: "attachDiskImage"
description: "Creates a transaction to attach a guest's disk image. If the disk image is already attached it will be ignored. 

WARNING: SoftLayer_Virtual_Guest::checkHostDiskAvailability should be called before this method. If the SoftLayer_Virtual_Guest::checkHostDiskAvailability method is not called before this method, the guest migration will happen automatically. "
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

### [REST Example](#attachDiskImage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#attachDiskImage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/attachDiskImage'
```

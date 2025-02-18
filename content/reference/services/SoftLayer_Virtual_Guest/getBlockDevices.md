---
title: "getBlockDevices"
description: "A computing instance's block devices. Block devices link [SoftLayer_Virtual_Disk_Image](/reference/datatypes/SoftLayer_Virtual_Disk_Image) to computing instances."
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

### [REST Example](#getBlockDevices-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBlockDevices-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getBlockDevices'
```

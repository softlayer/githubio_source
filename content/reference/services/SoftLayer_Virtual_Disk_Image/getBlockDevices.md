---
title: "getBlockDevices"
description: "The block devices that a disk image is attached to. Block devices connect computing instances to disk images."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Disk_Image"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Disk_Image"
---

### [REST Example](#getBlockDevices-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBlockDevices-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Disk_Image/{SoftLayer_Virtual_Disk_ImageID}/getBlockDevices'
```

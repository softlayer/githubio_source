---
title: "captureImage"
description: "Captures a Flex Image of the hard disk on the virtual machine, based on the capture template parameter. Returns the image template group containing the disk image. "
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

# [REST Example](#captureImage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#captureImage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Disk_Image_Capture_Template]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/captureImage'
```

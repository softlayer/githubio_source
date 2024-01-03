---
title: "captureImage"
description: "Captures an Image of the hard disk on the physical machine, based on the capture template parameter. Returns the image template group containing the disk image. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware"
---

# [REST Example](#captureImage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#captureImage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Disk_Image_Capture_Template]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware/{SoftLayer_HardwareID}/captureImage'
```

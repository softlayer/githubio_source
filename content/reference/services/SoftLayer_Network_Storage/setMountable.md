---
title: "setMountable"
description: "Enable or disable the mounting of a Storage volume. When mounting is enabled the Storage volume will be mountable or available for use. 

For Virtual Server volumes, disabling mounting will deny access to the Virtual Server Account, remove published material and deny all file interaction including uploads and downloads. 

Enabling or disabling mounting for Storage volumes is not possible if mounting has been disabled by SoftLayer or a parent account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/{SoftLayer_Network_StorageID}/setMountable'
```

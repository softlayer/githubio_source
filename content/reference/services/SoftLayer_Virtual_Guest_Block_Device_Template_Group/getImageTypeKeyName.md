---
title: "getImageTypeKeyName"
description: "The virtual disk image type keyname (e.g. SYSTEM, DISK_CAPTURE, ISO, etc) of this template. Value will be populated on parent and child, but only supports object filtering on the parent."
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

# [REST Example](#getImageTypeKeyName-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getImageTypeKeyName-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Block_Device_Template_Group/{SoftLayer_Virtual_Guest_Block_Device_Template_GroupID}/getImageTypeKeyName'
```

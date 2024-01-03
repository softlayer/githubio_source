---
title: "getMetadataFlag"
description: "Whether this disk image is meant for storage of custom user data supplied with a Cloud Computing Instance order."
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

# [REST Example](#getMetadataFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMetadataFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Disk_Image/{SoftLayer_Virtual_Disk_ImageID}/getMetadataFlag'
```

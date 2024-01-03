---
title: "getRemoteManagementComponent"
description: "A hardware's associated remote management component. This is normally IPMI."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule"
---

# [REST Example](#getRemoteManagementComponent-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRemoteManagementComponent-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/getRemoteManagementComponent'
```

---
title: "setOperatingSystemPassword"
description: "Changes the password that we have stored in our database for a servers' Operating System"
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

# [REST Example](#setOperatingSystemPassword-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setOperatingSystemPassword-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/setOperatingSystemPassword'
```

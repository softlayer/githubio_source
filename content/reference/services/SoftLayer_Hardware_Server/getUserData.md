---
title: "getUserData"
description: "An array containing a single string of custom user data for a hardware order. Max size is 16 kb."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Server"
---

# [REST Example](#getUserData-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getUserData-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/{SoftLayer_Hardware_ServerID}/getUserData'
```

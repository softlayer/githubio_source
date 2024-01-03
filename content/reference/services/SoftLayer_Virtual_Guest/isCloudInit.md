---
title: "isCloudInit"
description: "Determines if the virtual guest was provisioned from a cloud-init enabled image. "
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

# [REST Example](#isCloudInit-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#isCloudInit-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/isCloudInit'
```

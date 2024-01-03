---
title: "getActiveTransactions"
description: "Any active transaction(s) that are currently running for the server (example: os reload)."
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

# [REST Example](#getActiveTransactions-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getActiveTransactions-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/{SoftLayer_Hardware_ServerID}/getActiveTransactions'
```

---
title: "createArchiveTransaction"
description: "Create a transaction to archive a computing instance's block devices"
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

### [REST Example](#createArchiveTransaction-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createArchiveTransaction-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_Virtual_Guest_Block_Device, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/createArchiveTransaction'
```

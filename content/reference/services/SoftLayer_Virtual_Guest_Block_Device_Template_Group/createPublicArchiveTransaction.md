---
title: "createPublicArchiveTransaction"
description: "Create a transaction to copy archived block devices into public repository"
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

### [REST Example](#createPublicArchiveTransaction-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createPublicArchiveTransaction-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, string, SoftLayer_Location]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Block_Device_Template_Group/{SoftLayer_Virtual_Guest_Block_Device_Template_GroupID}/createPublicArchiveTransaction'
```

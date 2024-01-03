---
title: "removeLocations"
description: "This method will create transaction(s) to remove available locations from an archive image template."
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

# [REST Example](#removeLocations-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeLocations-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Location]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Block_Device_Template_Group/{SoftLayer_Virtual_Guest_Block_Device_Template_GroupID}/removeLocations'
```

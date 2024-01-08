---
title: "setAvailableLocations"
description: "Create transaction(s) to set the archived block device available locations"
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

### [REST Example](#setAvailableLocations-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setAvailableLocations-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Location]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Block_Device_Template_Group/{SoftLayer_Virtual_Guest_Block_Device_Template_GroupID}/setAvailableLocations'
```

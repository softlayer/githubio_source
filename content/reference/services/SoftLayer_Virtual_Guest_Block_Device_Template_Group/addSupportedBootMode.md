---
title: "addSupportedBootMode"
description: "This method allows you to mark this image's supported boot modes as 'HVM' or 'PV'. "
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

### [REST Example](#addSupportedBootMode-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addSupportedBootMode-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Block_Device_Template_Group/{SoftLayer_Virtual_Guest_Block_Device_Template_GroupID}/addSupportedBootMode'
```

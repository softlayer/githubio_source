---
title: "createFromExternalSource"
description: "Create a transaction to import a disk image from an external source and create a standard image template."
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

# [REST Example](#createFromExternalSource-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createFromExternalSource-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromExternalSource'
```

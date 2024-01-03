---
title: "createFromIcos"
description: "Create a process to import a disk image from ICOS and create a standard"
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

# [REST Example](#createFromIcos-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createFromIcos-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromIcos'
```

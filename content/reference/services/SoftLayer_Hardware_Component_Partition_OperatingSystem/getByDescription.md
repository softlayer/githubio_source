---
title: "getByDescription"
description: "The '''getByDescription''' method retrieves all possible partition templates based on the description (required parameter) entered when calling the method. The description is typically the operating system's name. Current recognized values include 'linux', 'windows', 'freebsd', and 'Debian'. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition_OperatingSystem"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Component_Partition_OperatingSystem"
---

### [REST Example](#getByDescription-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getByDescription-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Component_Partition_OperatingSystem/getByDescription'
```

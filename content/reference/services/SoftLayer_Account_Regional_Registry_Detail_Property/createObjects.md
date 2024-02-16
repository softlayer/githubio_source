---
title: "createObjects"
description: "The subnet registration detail property service has been deprecated. 

Edit multiple [SoftLayer_Account_Regional_Registry_Detail_Property](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property) objects. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail_Property"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Regional_Registry_Detail_Property"
---

### [REST Example](#createObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Regional_Registry_Detail_Property]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Regional_Registry_Detail_Property/createObjects'
```

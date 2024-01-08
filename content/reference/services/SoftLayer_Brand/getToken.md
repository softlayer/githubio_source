---
title: "getToken"
description: "(DEPRECATED) Use [SoftLayer_User_Customer::getImpersonationToken](/reference/datatypes/$1/#$2) method. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand"
type: "reference"
layout: "method"
mainService : "SoftLayer_Brand"
---

### [REST Example](#getToken-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getToken-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/{SoftLayer_BrandID}/getToken'
```

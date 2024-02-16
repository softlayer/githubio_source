---
title: "editObject"
description: "The subnet registration detail service has been deprecated. 

This method will edit an existing SoftLayer_Account_Regional_Registry_Detail object. For more detail, see [SoftLayer_Account_Regional_Registry_Detail::createObject](/reference/datatypes/$1/#$2). "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Regional_Registry_Detail"
---

### [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Regional_Registry_Detail]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Regional_Registry_Detail/{SoftLayer_Account_Regional_Registry_DetailID}/editObject'
```

---
title: "addAchInformation"
description: ""
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Billing_Info_Ach]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/addAchInformation'
```

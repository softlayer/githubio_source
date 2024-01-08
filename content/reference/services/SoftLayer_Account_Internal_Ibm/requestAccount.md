---
title: "requestAccount"
description: "Validates request and kicks off the approval process. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Internal_Ibm"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Internal_Ibm"
---

### [REST Example](#requestAccount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#requestAccount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Account_Internal_Ibm_Request]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Internal_Ibm/requestAccount'
```

---
title: "hasAttribute"
description: "Determine if an account has an [SoftLayer_Account_Attribute](/reference/datatypes/SoftLayer_Account_Attribute) associated with it. hasAttribute() returns false if the attribute does not exist or if it does not have a value. "
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

### [REST Example](#hasAttribute-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#hasAttribute-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/hasAttribute'
```

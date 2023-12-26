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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/hasAttribute'
```

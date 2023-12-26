---
title: "changePreference"
description: "Select a type of preference you would like to modify using [SoftLayer_User_Customer::getPreferenceTypes](/reference/datatypes/$1/#$2) and invoke this method using that preference type key name. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/changePreference'
```

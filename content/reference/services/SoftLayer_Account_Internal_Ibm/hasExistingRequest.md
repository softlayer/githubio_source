---
title: "hasExistingRequest"
description: "Checks for an existing request which would block an IBMer from submitting a new request. Such a request could be denied, approved, or awaiting manager action. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Internal_Ibm/hasExistingRequest'
```

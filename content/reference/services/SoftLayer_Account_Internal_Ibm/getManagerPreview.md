---
title: "getManagerPreview"
description: "After validating the requesting user through the access token, generates a container with the relevant request information and returns it. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Internal_Ibm/getManagerPreview'
```

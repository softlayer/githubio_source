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

# [REST Example](#getManagerPreview-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getManagerPreview-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Internal_Ibm/getManagerPreview'
```

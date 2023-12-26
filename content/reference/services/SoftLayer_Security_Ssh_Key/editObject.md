---
title: "editObject"
description: "Update a ssh key. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Ssh_Key"
type: "reference"
layout: "method"
mainService : "SoftLayer_Security_Ssh_Key"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Security_Ssh_Key]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Ssh_Key/{SoftLayer_Security_Ssh_KeyID}/editObject'
```

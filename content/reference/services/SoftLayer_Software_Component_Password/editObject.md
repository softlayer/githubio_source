---
title: "editObject"
description: "Edit the properties of a software component password such as the username, password, port, and notes. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_Password"
type: "reference"
layout: "method"
mainService : "SoftLayer_Software_Component_Password"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Software_Component_Password]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Software_Component_Password/{SoftLayer_Software_Component_PasswordID}/editObject'
```

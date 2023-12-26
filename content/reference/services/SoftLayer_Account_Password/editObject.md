---
title: "editObject"
description: "The password and/or notes may be modified.  Modifying the EVault passwords here will also update the password the Webcc interface will use. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Password"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Password"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Password]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Password/{SoftLayer_Account_PasswordID}/editObject'
```

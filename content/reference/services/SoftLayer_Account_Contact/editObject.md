---
title: "editObject"
description: "This method allows you to modify an account contact. Only master users are permitted to modify an account contact. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Contact"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Contact"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Contact]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Contact/{SoftLayer_Account_ContactID}/editObject'
```

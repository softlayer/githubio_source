---
title: "editObject"
description: "Edit the properties of an address record by passing in a modified instance of a SoftLayer_Account_Address object. Users will be restricted to modifying addresses for their account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Address"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Address"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Address]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Address/{SoftLayer_Account_AddressID}/editObject'
```

---
title: "editObject"
description: "Edit the properties of customer ApiAuthentication record by passing in a modified instance of a SoftLayer_User_Customer_ApiAuthentication object. Only the ipAddressRestriction property can be modified. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_ApiAuthentication"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_ApiAuthentication"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Customer_ApiAuthentication]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_ApiAuthentication/{SoftLayer_User_Customer_ApiAuthenticationID}/editObject'
```

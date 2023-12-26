---
title: "getUser"
description: "The user who owns the api authentication key."
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_ApiAuthentication/{SoftLayer_User_Customer_ApiAuthenticationID}/getUser'
```

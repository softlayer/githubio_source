---
title: "getAuthenticationToken"
description: "This method generate user authentication token and return [SoftLayer_Container_User_Authentication_Token](/reference/datatypes/SoftLayer_Container_User_Authentication_Token) object which will be used to authenticate user to login to SoftLayer customer portal. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_User_Authentication_Token]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/{SoftLayer_User_Customer_OpenIdConnect_TrustedProfileID}/getAuthenticationToken'
```

---
title: "getLoginToken"
description: "Attempt to authenticate a user to the SoftLayer customer portal using the provided authentication container. Depending on the specific type of authentication container that is used, this API will leverage the appropriate authentication protocol. If authentication is successful then the API returns a list of linked accounts for the user, a token containing the ID of the authenticated user and a hash key used by the SoftLayer customer portal to maintain authentication. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Authentication_Request_Contract]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/getLoginToken'
```

---
title: "getPortalLoginToken"
description: "Attempt to authenticate a username and password to the SoftLayer customer portal. Many portal user accounts are configured to require answering a security question on login. In this case getPortalLoginToken() also verifies the given security question ID and answer. If authentication is successful then the API returns a token containing the ID of the authenticated user and a hash key used by the SoftLayer customer portal to maintain authentication. "
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

### [REST Example](#getPortalLoginToken-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPortalLoginToken-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/getPortalLoginToken'
```

---
title: "getPortalLoginTokenOpenIdConnect"
description: "Attempt to authenticate a supplied OpenIdConnect access token to the SoftLayer customer portal. If authentication is successful then the API returns a token containing the ID of the authenticated user and a hash key used by the SoftLayer customer portal to maintain authentication. "
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

### [REST Example](#getPortalLoginTokenOpenIdConnect-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPortalLoginTokenOpenIdConnect-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, int, int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/getPortalLoginTokenOpenIdConnect'
```

---
title: "getLoginAccountInfoOpenIdConnect"
description: "Validates a supplied OpenIdConnect access token to the SoftLayer customer portal and returns the default account name and id for the active user. An exception will be thrown if no matching customer is found. "
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

### [REST Example](#getLoginAccountInfoOpenIdConnect-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getLoginAccountInfoOpenIdConnect-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/getLoginAccountInfoOpenIdConnect'
```

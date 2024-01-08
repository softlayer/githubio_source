---
title: "setDefaultAccount"
description: "An OpenIdConnect identity, for example an IAMid, can be linked or mapped to one or more individual SoftLayer users, but no more than one per account. If an OpenIdConnect identity is mapped to multiple accounts in this manner, one such account should be identified as the default account for that identity. Invoke this only on IBMid-authenticated users. "
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

### [REST Example](#setDefaultAccount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setDefaultAccount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/{SoftLayer_User_Customer_OpenIdConnect_TrustedProfileID}/setDefaultAccount'
```

---
title: "getUnsuccessfulLogins"
description: "A user's unsuccessful attempts to log into the SoftLayer customer portal."
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

### [REST Example](#getUnsuccessfulLogins-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getUnsuccessfulLogins-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/{SoftLayer_User_Customer_OpenIdConnect_TrustedProfileID}/getUnsuccessfulLogins'
```

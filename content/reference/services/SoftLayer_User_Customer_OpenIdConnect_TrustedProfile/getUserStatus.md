---
title: "getUserStatus"
description: "A portal user's status, which controls overall access to the SoftLayer customer portal and VPN access to the private network."
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

# [REST Example](#getUserStatus-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getUserStatus-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/{SoftLayer_User_Customer_OpenIdConnect_TrustedProfileID}/getUserStatus'
```

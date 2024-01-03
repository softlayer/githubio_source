---
title: "turnOnMasterUserPermissionCheckMode"
description: "This method allows the master user of an account to designate this user as an alternate master user.  Effectively this means that this user should have 'all the same IMS permissions as a master user'. 

Note that this method, by itself, WILL NOT affect the IAM Policies granted to this user. This API is not intended for general customer use.  It is intended to be called by IAM, in concert with other actions taken by IAM when the master user / account owner designates an 'alternate/auxiliary master user / account owner'. "
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

# [REST Example](#turnOnMasterUserPermissionCheckMode-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#turnOnMasterUserPermissionCheckMode-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/turnOnMasterUserPermissionCheckMode'
```

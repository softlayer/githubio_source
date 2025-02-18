---
title: "getUserForUnifiedInvitation"
description: "Returns an IMS User Object from the provided OpenIdConnect User ID or IBMid Unique Identifier for the Account of the active user. Enforces the User Management permissions for the Active User. An exception will be thrown if no matching IMS User is found. NOTE that providing IBMid Unique Identifier is optional, but it will be preferred over OpenIdConnect User ID if provided. "
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

### [REST Example](#getUserForUnifiedInvitation-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getUserForUnifiedInvitation-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/getUserForUnifiedInvitation'
```

---
title: "completeInvitationAfterLogin"
description: "Completes invitation processing after logging on an existing OpenIdConnect user identity and return an access token"
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

### [REST Example](#completeInvitationAfterLogin-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#completeInvitationAfterLogin-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/completeInvitationAfterLogin'
```

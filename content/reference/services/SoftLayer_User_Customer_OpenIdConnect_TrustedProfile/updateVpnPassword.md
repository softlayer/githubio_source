---
title: "updateVpnPassword"
description: "Update a user's VPN password on the SoftLayer customer portal. As with portal passwords, VPN passwords must match the following restrictions. VPN passwords must... 
* ...be over eight characters long.
* ...be under twenty characters long.
* ...contain at least one uppercase letter
* ...contain at least one lowercase letter
* ...contain at least one number
* ...contain one of the special characters _ - | @ . , ? / ! ~ # $ % ^ & * ( ) { } [ ] \ =
* ...not match your username
Finally, users can only update their own VPN password. An account's master user can update any of their account users' VPN passwords. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/{SoftLayer_User_Customer_OpenIdConnect_TrustedProfileID}/updateVpnPassword'
```

---
title: "turnOffMasterUserPermissionCheckMode"
description: "This method allows the master user of an account to undo the designation of this user as an alternate master user.  This can not be applied to the true master user of the account. 

Note that this method, by itself, WILL NOT affect the IAM Policies granted this user.  This API is not intended for general customer use.  It is intended to be called by IAM, in concert with other actions taken by IAM when the master user / account owner turns off an 'alternate/auxiliary master user / account owner'. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/turnOffMasterUserPermissionCheckMode'
```

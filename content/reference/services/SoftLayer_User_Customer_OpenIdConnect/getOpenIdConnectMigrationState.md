---
title: "getOpenIdConnectMigrationState"
description: "This API returns a SoftLayer_Container_User_Customer_OpenIdConnect_MigrationState object containing the necessary information to determine what migration state the user is in. If the account is not OpenIdConnect authenticated, then an exception is thrown. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/getOpenIdConnectMigrationState'
```

---
title: "silentlyMigrateUserOpenIdConnect"
description: "As master user, calling this api for the IBMid provider type when there is an existing IBMid for the email on the SL account will silently (without sending an invitation email) create a link for the IBMid. NOTE: If the SoftLayer user is already linked to IBMid, this call will fail. If the IBMid specified by the email of this user, is already used in a link to another user in this account, this call will fail. If there is already an open invitation from this SoftLayer user to this or any IBMid, this call will fail. If there is already an open invitation from some other SoftLayer user in this account to this IBMid, then this call will fail. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/silentlyMigrateUserOpenIdConnect'
```

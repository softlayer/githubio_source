---
title: "getVirtualGuestCount"
description: "Retrieve the number of CloudLayer Computing Instances that a portal user has access to. Portal users can have restrictions set to limit services for and to perform actions on CloudLayer Computing Instances. You can set these permissions in the portal by clicking the 'administrative' then 'user admin' links. "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/{SoftLayer_User_Customer_OpenIdConnect_TrustedProfileID}/getVirtualGuestCount'
```

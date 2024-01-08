---
title: "getVirtualGuests"
description: "A portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing Instances a user has access to in the SoftLayer customer portal."
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

### [REST Example](#getVirtualGuests-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getVirtualGuests-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/getVirtualGuests'
```

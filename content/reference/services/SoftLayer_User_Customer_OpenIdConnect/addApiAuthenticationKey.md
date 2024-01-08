---
title: "addApiAuthenticationKey"
description: "Create a user's API authentication key, allowing that user access to query the SoftLayer API. addApiAuthenticationKey() returns the user's new API key. Each portal user is allowed only one API key. "
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

### [REST Example](#addApiAuthenticationKey-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addApiAuthenticationKey-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/addApiAuthenticationKey'
```

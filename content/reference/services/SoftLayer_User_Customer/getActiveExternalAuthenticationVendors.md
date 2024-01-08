---
title: "getActiveExternalAuthenticationVendors"
description: "The getActiveExternalAuthenticationVendors method will return a list of available external vendors that a SoftLayer user can authenticate against.  The list will only contain vendors for which the user has at least one active external binding. "
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

### [REST Example](#getActiveExternalAuthenticationVendors-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getActiveExternalAuthenticationVendors-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/getActiveExternalAuthenticationVendors'
```

---
title: "getAllObjects"
description: "getAllObjects() will return a list of the available external binding vendors that SoftLayer supports.  Use this list to select the appropriate vendor when creating a new external binding. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_External_Binding_Vendor"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_External_Binding_Vendor"
---

### [REST Example](#getAllObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_External_Binding_Vendor/getAllObjects'
```

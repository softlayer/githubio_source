---
title: "getPreference"
description: "Select a type of preference you would like to get using [SoftLayer_User_Customer::getPreferenceTypes](/reference/datatypes/$1/#$2) and invoke this method using that preference type key name. "
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

# [REST Example](#getPreference-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPreference-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/getPreference'
```

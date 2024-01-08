---
title: "removeApiAuthenticationKey"
description: "Remove a user's API authentication key, removing that user's access to query the SoftLayer API. "
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

### [REST Example](#removeApiAuthenticationKey-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeApiAuthenticationKey-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/removeApiAuthenticationKey'
```

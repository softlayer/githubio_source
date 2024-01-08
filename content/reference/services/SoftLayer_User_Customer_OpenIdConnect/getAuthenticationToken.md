---
title: "getAuthenticationToken"
description: "This method generate user authentication token and return [SoftLayer_Container_User_Authentication_Token](/reference/datatypes/SoftLayer_Container_User_Authentication_Token) object which will be used to authenticate user to login to SoftLayer customer portal. "
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

### [REST Example](#getAuthenticationToken-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAuthenticationToken-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_User_Authentication_Token]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/getAuthenticationToken'
```

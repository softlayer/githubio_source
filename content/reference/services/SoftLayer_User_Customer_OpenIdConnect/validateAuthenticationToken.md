---
title: "validateAuthenticationToken"
description: "This method validate the given authentication token using the user id by comparing it with the actual user authentication token and return [SoftLayer_Container_User_Customer_Portal_Token](/reference/datatypes/SoftLayer_Container_User_Customer_Portal_Token) object "
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

### [REST Example](#validateAuthenticationToken-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#validateAuthenticationToken-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_User_Authentication_Token]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/validateAuthenticationToken'
```

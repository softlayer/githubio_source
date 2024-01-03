---
title: "getHasFullHardwareAccessFlag"
description: "Whether or not a portal user has access to all hardware on their account."
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

# [REST Example](#getHasFullHardwareAccessFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getHasFullHardwareAccessFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/getHasFullHardwareAccessFlag'
```

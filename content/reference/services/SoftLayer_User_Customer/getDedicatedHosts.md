---
title: "getDedicatedHosts"
description: "The dedicated hosts to which the user has been granted access."
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

### [REST Example](#getDedicatedHosts-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getDedicatedHosts-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/getDedicatedHosts'
```

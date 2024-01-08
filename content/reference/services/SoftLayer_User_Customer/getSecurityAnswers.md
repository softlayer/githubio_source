---
title: "getSecurityAnswers"
description: "A portal user's security question answers. Some portal users may not have security answers or may not be configured to require answering a security question on login."
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

### [REST Example](#getSecurityAnswers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSecurityAnswers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/getSecurityAnswers'
```

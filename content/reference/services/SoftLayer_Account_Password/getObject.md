---
title: "getObject"
description: "getObject retrieves the SoftLayer_Account_Password object whose ID corresponds to the ID number of the init parameter passed to the SoftLayer_Account_Password service. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Password"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Password"
---

### [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Password/{SoftLayer_Account_PasswordID}/getObject'
```

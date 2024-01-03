---
title: "editObject"
description: "The password and/or notes may be modified.  Modifying the EVault passwords here will also update the password the Webcc interface will use. "
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

# [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Password]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Password/{SoftLayer_Account_PasswordID}/editObject'
```

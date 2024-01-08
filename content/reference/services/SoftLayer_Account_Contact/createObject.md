---
title: "createObject"
description: "This method creates an account contact. The accountId is fixed, other properties can be set during creation. The typeId indicates the SoftLayer_Account_Contact_Type for the contact. This method returns the SoftLayer_Account_Contact object that is created. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Contact"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Contact"
---

### [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Contact]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Contact/createObject'
```

---
title: "deleteObject"
description: "deleteObject permanently removes an account link and all of it's associated keystone data (including users for the associated project). '''This cannot be undone.''' Be wary of running this method. If you remove an account link in error you will need to re-create it by creating a new SoftLayer_Account_Link_OpenStack object. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Link_OpenStack"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Link_OpenStack"
---

### [REST Example](#deleteObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Link_OpenStack/{SoftLayer_Account_Link_OpenStackID}/deleteObject'
```

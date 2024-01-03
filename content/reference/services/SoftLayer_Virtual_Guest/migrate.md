---
title: "migrate"
description: "Creates a transaction to migrate a virtual guest to a new host. NOTE: Will only migrate if SoftLayer_Virtual_Guest property pendingMigrationFlag = true"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

# [REST Example](#migrate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#migrate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/migrate'
```

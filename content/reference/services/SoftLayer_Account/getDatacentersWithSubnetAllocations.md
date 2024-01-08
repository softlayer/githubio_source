---
title: "getDatacentersWithSubnetAllocations"
description: "Datacenters which contain subnets that the account has access to route."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

### [REST Example](#getDatacentersWithSubnetAllocations-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getDatacentersWithSubnetAllocations-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getDatacentersWithSubnetAllocations'
```

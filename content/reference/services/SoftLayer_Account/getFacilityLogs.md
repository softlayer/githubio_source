---
title: "getFacilityLogs"
description: "Logs of who entered a colocation area which is assigned to this account, or when a user under this account enters a datacenter."
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

### [REST Example](#getFacilityLogs-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getFacilityLogs-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getFacilityLogs'
```

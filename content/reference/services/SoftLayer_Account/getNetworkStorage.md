---
title: "getNetworkStorage"
description: "An account's associated storage volumes. This includes Lockbox, NAS, EVault, and iSCSI volumes."
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

### [REST Example](#getNetworkStorage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getNetworkStorage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getNetworkStorage'
```

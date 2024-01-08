---
title: "getNextBillingCycleBandwidthAllocation"
description: "A hardware's allotted bandwidth for the next billing cycle (measured in GB)."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule"
---

### [REST Example](#getNextBillingCycleBandwidthAllocation-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getNextBillingCycleBandwidthAllocation-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/getNextBillingCycleBandwidthAllocation'
```

---
title: "getBillingCycleBandwidthUsage"
description: "The raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to."
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

### [REST Example](#getBillingCycleBandwidthUsage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBillingCycleBandwidthUsage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getBillingCycleBandwidthUsage'
```

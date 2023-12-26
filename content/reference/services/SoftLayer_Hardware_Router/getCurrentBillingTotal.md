---
title: "getCurrentBillingTotal"
description: "Get the total bill amount in US Dollars ($) for this hardware in the current billing period. This includes all bandwidth used up to the point the method is called on the hardware. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Router"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Router/{SoftLayer_Hardware_RouterID}/getCurrentBillingTotal'
```

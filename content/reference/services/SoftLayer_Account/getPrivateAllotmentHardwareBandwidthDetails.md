---
title: "getPrivateAllotmentHardwareBandwidthDetails"
description: "DEPRECATED - This information can be pulled directly through tapping keys now - DEPRECATED. The allotments for this account and their servers. The private inbound and outbound bandwidth is calculated for each server in addition to the daily average network traffic since the last billing date."
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getPrivateAllotmentHardwareBandwidthDetails'
```

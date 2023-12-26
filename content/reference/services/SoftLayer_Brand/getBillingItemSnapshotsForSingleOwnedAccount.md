---
title: "getBillingItemSnapshotsForSingleOwnedAccount"
description: "This service returns the snapshots of billing items recorded periodically given an account ID. The provided account ID must be owned by the brand that calls this service. In this context, it can be interpreted that the billing items snapshots belong to both the account and that accounts brand. Retrieving billing item snapshots is more performant than retrieving billing items directly and performs less relational joins improving retrieval efficiency. 

The downside is, they are not real time, and do not share relational parity with the original billing item. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand"
type: "reference"
layout: "method"
mainService : "SoftLayer_Brand"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/{SoftLayer_BrandID}/getBillingItemSnapshotsForSingleOwnedAccount'
```

---
title: "getUpgradeItemPrices"
description: "Retrieve a list of upgradeable items available to this piece of hardware. Currently, getUpgradeItemPrices retrieves upgrades available for a server's memory, hard drives, network port speed, bandwidth allocation and GPUs. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware/{SoftLayer_HardwareID}/getUpgradeItemPrices'
```

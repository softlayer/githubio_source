---
title: "updateMaintenanceWindow"
description: "In case an upgrade cannot be performed, the maintenance window needs to be updated to a future date. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Upgrade_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Upgrade_Request"
---

### [REST Example](#updateMaintenanceWindow-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateMaintenanceWindow-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Upgrade_Request/{SoftLayer_Product_Upgrade_RequestID}/updateMaintenanceWindow'
```

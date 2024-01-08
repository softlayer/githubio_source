---
title: "getMaintenanceWindowForTicket"
description: "Returns a specific maintenance window. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Provisioning"
classes:
    - "SoftLayer_Provisioning_Maintenance_Window"
type: "reference"
layout: "method"
mainService : "SoftLayer_Provisioning_Maintenance_Window"
---

### [REST Example](#getMaintenanceWindowForTicket-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMaintenanceWindowForTicket-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Provisioning_Maintenance_Window/getMaintenanceWindowForTicket'
```

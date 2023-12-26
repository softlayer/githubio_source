---
title: "getMaintenanceWindowTicketsByTicketId"
description: "getMaintenanceWindowTicketsByTicketId() returns a list maintenance window ticket records by ticket id "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Provisioning_Maintenance_Window/getMaintenanceWindowTicketsByTicketId'
```

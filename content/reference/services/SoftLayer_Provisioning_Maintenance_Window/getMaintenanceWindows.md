---
title: "getMaintenanceWindows"
description: "This method returns a list of available maintenance windows "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime, int, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Provisioning_Maintenance_Window/getMaintenanceWindows'
```

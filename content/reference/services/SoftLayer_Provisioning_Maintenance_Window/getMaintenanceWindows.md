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

### [REST Example](#getMaintenanceWindows-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMaintenanceWindows-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime, int, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Provisioning_Maintenance_Window/getMaintenanceWindows'
```

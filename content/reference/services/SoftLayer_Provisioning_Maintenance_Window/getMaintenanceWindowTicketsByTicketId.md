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

# [REST Example](#getMaintenanceWindowTicketsByTicketId-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMaintenanceWindowTicketsByTicketId-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Provisioning_Maintenance_Window/getMaintenanceWindowTicketsByTicketId'
```

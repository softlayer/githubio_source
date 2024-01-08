---
title: "getActiveTickets"
description: "The active tickets that are attached to the MDMS request."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_MassDataMigration_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_MassDataMigration_Request"
---

### [REST Example](#getActiveTickets-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getActiveTickets-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_MassDataMigration_Request/{SoftLayer_Network_Storage_MassDataMigration_RequestID}/getActiveTickets'
```

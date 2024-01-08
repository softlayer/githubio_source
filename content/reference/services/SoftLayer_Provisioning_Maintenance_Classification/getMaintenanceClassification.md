---
title: "getMaintenanceClassification"
description: "Retrieve an array of SoftLayer_Provisioning_Maintenance_Classification data types, which contain all maintenance classifications. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Provisioning"
classes:
    - "SoftLayer_Provisioning_Maintenance_Classification"
type: "reference"
layout: "method"
mainService : "SoftLayer_Provisioning_Maintenance_Classification"
---

### [REST Example](#getMaintenanceClassification-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMaintenanceClassification-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Provisioning_Maintenance_Classification/getMaintenanceClassification'
```

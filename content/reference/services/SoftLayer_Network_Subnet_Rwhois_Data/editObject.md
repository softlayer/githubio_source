---
title: "editObject"
description: "Edit the RWHOIS record by passing in a modified version of the record object.  All fields are editable."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Rwhois_Data"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_Rwhois_Data"
---

# [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Subnet_Rwhois_Data]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Rwhois_Data/{SoftLayer_Network_Subnet_Rwhois_DataID}/editObject'
```

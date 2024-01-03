---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Subnet_Rwhois_Data object whose ID corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Subnet_Rwhois_Data service. 

The best way to get Rwhois Data for an account is through getRhwoisData on the Account service. "
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

# [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Rwhois_Data/{SoftLayer_Network_Subnet_Rwhois_DataID}/getObject'
```

---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Storage object whose ID corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Storage service. 

Please use the associated methods in the [SoftLayer_Network_Storage](/reference/datatypes/SoftLayer_Network_Storage) service to retrieve a Storage account's id. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage"
---

# [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/{SoftLayer_Network_StorageID}/getObject'
```

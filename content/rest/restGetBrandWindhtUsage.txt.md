---
title: "restGetBrandWindhtUsage.txt"
description: "restGetBrandWindhtUsage.txt"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
https://$USERNAME:$APIKEY@api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/$SERVERID/getObject.json?objectMask=mask[hostname,currentBillableBandwidthUsage]

method : GET
```

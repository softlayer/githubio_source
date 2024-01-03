---
title: "checkConnection"
description: "DEPRECATED. Checks if a monitoring robot can communicate with SoftLayer monitoring management system via the private network. 

TCP port 48000 - 48002 must be open on your server or your virtual server in order for this test to succeed. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Robot"
type: "reference"
layout: "method"
mainService : "SoftLayer_Monitoring_Robot"
---

# [REST Example](#checkConnection-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#checkConnection-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Monitoring_Robot/{SoftLayer_Monitoring_RobotID}/checkConnection'
```

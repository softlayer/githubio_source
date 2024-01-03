---
title: "upgradeConnectionLimit"
description: "Upgrades the connection limit on the VirtualIp and changes the billing item on your account to reflect the change. This function will only upgrade you to the next 'level' of service.  The next level follows this pattern Current Level  =>  Next Level 50                 100 100                200 200                500 500                1000 1000               1200 1200               1500 1500               2000 2000               2500 2500               3000 "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
---

# [REST Example](#upgradeConnectionLimit-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#upgradeConnectionLimit-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_VirtualIpAddress/{SoftLayer_Network_LoadBalancer_VirtualIpAddressID}/upgradeConnectionLimit'
```

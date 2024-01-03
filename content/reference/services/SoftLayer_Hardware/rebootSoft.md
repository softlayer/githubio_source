---
title: "rebootSoft"
description: "The '''rebootSoft''' method reboots the server by issuing a reset command to the server's remote management card via soft reboot. When executing a soft reboot, servers allow all processes to shut down completely before rebooting. Remote management commands are unable to be issued within 20 minutes of issuing a successful soft reboot in order to avoid server failure. Remote management commands include: 

rebootSoft rebootHard powerOn powerOff powerCycle 

"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware"
---

# [REST Example](#rebootSoft-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#rebootSoft-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware/{SoftLayer_HardwareID}/rebootSoft'
```

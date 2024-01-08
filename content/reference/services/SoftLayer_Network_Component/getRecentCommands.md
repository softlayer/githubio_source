---
title: "getRecentCommands"
description: "The last five reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) commands issued to the server's remote management card."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Component"
---

### [REST Example](#getRecentCommands-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRecentCommands-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Component/{SoftLayer_Network_ComponentID}/getRecentCommands'
```

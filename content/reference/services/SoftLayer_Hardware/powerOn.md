---
title: "powerOn"
description: "The '''powerOn''' method powers on a server via its remote management card. This boolean return value returns ''true'' upon successful execution and ''false'' if unsuccessful. Other remote management commands may not be issued in this command was successfully completed within the last 20 minutes to avoid server failure. Remote management commands include: 

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

### [REST Example](#powerOn-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#powerOn-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware/{SoftLayer_HardwareID}/powerOn'
```

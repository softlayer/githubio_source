---
title: "rebootHard"
description: "The '''rebootHard''' method reboots the server by issuing a cycle command to the server's remote management card. A hard reboot is equivalent to pressing the ''Reset'' button on a server - it is issued immediately and will not allow processes to shut down prior to the reboot. Completing a hard reboot may initiate system disk checks upon server reboot, causing the boot up to take longer than normally expected. 

Remote management commands are unable to be executed if a reboot has been issued successfully within the last 20 minutes to avoid server failure. Remote management commands include: 

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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware/{SoftLayer_HardwareID}/rebootHard'
```

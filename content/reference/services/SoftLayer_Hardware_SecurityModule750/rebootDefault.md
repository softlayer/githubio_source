---
title: "rebootDefault"
description: "Attempts to reboot the server by issuing a reset (soft reboot) command to the server's remote management card. If the reset (soft reboot) attempt is unsuccessful, a power cycle command will be issued via the powerstrip. The power cycle command is equivalent to unplugging the server from the powerstrip and then plugging the server back into the powerstrip.  If a reboot command has been issued successfully in the past 20 minutes, another remote management command (rebootSoft, rebootHard, powerOn, powerOff and powerCycle) will not be allowed.  This is to avoid any type of server failures. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule750"
---

### [REST Example](#rebootDefault-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#rebootDefault-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/rebootDefault'
```

---
title: "rebootHard"
description: "Reboot the server by issuing a cycle command to the server's remote management card.  This is equivalent to pressing the 'Reset' button on the server.  This command is issued immediately and will not wait for processes to shutdown. After this command is issued, the server may take a few moments to boot up as server may run system disks checks. If a reboot command has been issued successfully in the past 20 minutes, another remote management command (rebootSoft, rebootHard, powerOn, powerOff and powerCycle) will not be allowed.  This is to avoid any type of server failures. "
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

### [REST Example](#rebootHard-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#rebootHard-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/rebootHard'
```

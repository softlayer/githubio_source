---
title: "verifyReloadOperatingSystem"
description: "Verify that a virtual server can go through the operating system reload process. It may be useful to call this method before attempting to actually reload the operating system just to verify that the reload will go smoothly. If the server configuration is not setup correctly or there is some other issue, an exception will be thrown indicating the error. If there were no issues, this will just return true. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

### [REST Example](#verifyReloadOperatingSystem-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#verifyReloadOperatingSystem-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Hardware_Server_Configuration]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/verifyReloadOperatingSystem'
```

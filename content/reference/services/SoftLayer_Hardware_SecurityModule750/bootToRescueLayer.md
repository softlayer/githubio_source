---
title: "bootToRescueLayer"
description: "The Rescue Kernel is designed to provide you with the ability to bring a server online in order to troubleshoot system problems that would normally only be resolved by an OS Reload. The correct Rescue Kernel will be selected based upon the currently installed operating system. When the rescue kernel process is initiated, the server will shutdown and reboot on to the public network with the same IP's assigned to the server to allow for remote connections. It will bring your server offline for approximately 10 minutes while the rescue is in progress. The root/administrator password will be the same as what is listed in the portal for the server. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/bootToRescueLayer'
```

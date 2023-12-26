---
title: "getWindowsUpdateStatus"
description: "This method returns an update status record for this server.  That record will specify if the server is missing updates, or has updates that must be reinstalled or require a reboot to go into affect. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/getWindowsUpdateStatus'
```

---
title: "getWindowsUpdateInstalledUpdates"
description: "Retrieve a list of Windows updates installed on a server as reported by the local SoftLayer Windows Server Update Services (WSUS) server. Windows servers provisioned by SoftLayer are configured to use the local WSUS server via the private network by default. "
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

### [REST Example](#getWindowsUpdateInstalledUpdates-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getWindowsUpdateInstalledUpdates-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/getWindowsUpdateInstalledUpdates'
```

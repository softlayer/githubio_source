---
title: "getWindowsUpdateStatus"
description: "Retrieve a list of an account's hardware's Windows Update status. This list includes which servers have available updates, which servers require rebooting due to updates, which servers have failed retrieving updates, and which servers have failed to communicate with the SoftLayer private Windows Software Update Services server. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getWindowsUpdateStatus'
```

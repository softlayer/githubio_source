---
title: "getCurrentBenchmarkCertificationResultFile"
description: "Attempt to retrieve the file associated with the current benchmark certification result, if such a file exists.  If there is no file for this benchmark certification result, calling this method throws an exception. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/getCurrentBenchmarkCertificationResultFile'
```

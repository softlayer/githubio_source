---
title: "getCurrentBenchmarkCertificationResultFile"
description: "Attempt to retrieve the file associated with the current benchmark certification result, if such a file exists.  If there is no file for this benchmark certification result, calling this method throws an exception. "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/getCurrentBenchmarkCertificationResultFile'
```

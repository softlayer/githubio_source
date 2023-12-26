---
title: "createObject"
description: "Create a new vulnerability scan request. New scan requests are picked up every five minutes, and the time to complete an actual scan may vary. Once the scan is finished, it can take up to another five minutes for the report to be generated and accessible. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Security_Scanner_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Security_Scanner_Request"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Security_Scanner_Request]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Security_Scanner_Request/createObject'
```

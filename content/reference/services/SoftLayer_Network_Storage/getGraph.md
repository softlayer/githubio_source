---
title: "getGraph"
description: "{{CloudLayerOnlyMethod}} 

getGraph() retrieves a Storage account's usage and returns a PNG graph image, title, and the minimum and maximum dates included in the graphed date range. Virtual Server storage accounts can also graph upload and download bandwidth usage. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/{SoftLayer_Network_StorageID}/getGraph'
```

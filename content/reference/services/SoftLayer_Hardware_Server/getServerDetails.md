---
title: "getServerDetails"
description: "Retrieve a server's hardware components, software, and network components. getServerDetails is an aggregation function that combines the results of [SoftLayer_Hardware_Server::getComponents](/reference/datatypes/$1/#$2), [SoftLayer_Hardware_Server::getSoftware](/reference/datatypes/$1/#$2), and [SoftLayer_Hardware_Server::getNetworkComponents](/reference/datatypes/$1/#$2) in a single container. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Server"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/{SoftLayer_Hardware_ServerID}/getServerDetails'
```

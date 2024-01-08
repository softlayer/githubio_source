---
title: "collectBandwidth"
description: "{{CloudLayerOnlyMethod}} 

collectBandwidth() Retrieve the bandwidth usage for the current billing cycle. "
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

### [REST Example](#collectBandwidth-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#collectBandwidth-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/{SoftLayer_Network_StorageID}/collectBandwidth'
```

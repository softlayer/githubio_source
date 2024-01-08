---
title: "initiateOriginVolumeReclaim"
description: "Initiates Origin Volume Reclaim to delete volume from NetApp."
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

### [REST Example](#initiateOriginVolumeReclaim-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#initiateOriginVolumeReclaim-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/{SoftLayer_Network_StorageID}/initiateOriginVolumeReclaim'
```

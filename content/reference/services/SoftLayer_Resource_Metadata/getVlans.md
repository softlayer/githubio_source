---
title: "getVlans"
description: "The getVlans method returns a list of VLAN numbers for the network component matching the provided MAC address associated with the resource. For each return, the native VLAN will appear first, followed by any trunked VLANs associated with the network component. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Metadata"
type: "reference"
layout: "method"
mainService : "SoftLayer_Resource_Metadata"
---

### [REST Example](#getVlans-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getVlans-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Resource_Metadata/{SoftLayer_Resource_MetadataID}/getVlans'
```

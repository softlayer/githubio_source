---
title: "getServiceResources"
description: "The getServiceResources method retrieves all service resources associated with the resource. Service resources are additional resources that may be used by this resource. The output format is <type>=<address> for each service resource. "
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

# [REST Example](#getServiceResources-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getServiceResources-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Resource_Metadata/{SoftLayer_Resource_MetadataID}/getServiceResources'
```

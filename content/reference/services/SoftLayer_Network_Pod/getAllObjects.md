---
title: "getAllObjects"
description: "Filtering is supported for ``datacenterName`` and ``capabilities``. When filtering on capabilities, use the ``in`` operation. Pods fulfilling all capabilities provided will be returned. ``datacenterName`` represents an operation against ``SoftLayer_Location_Datacenter.name`, such as dal05 when referring to Dallas 5. 

```Examples:``` 

List Pods in a specific datacenter. <pre> datacenterName.operation = 'dal06' </pre> 

List Pods in a geographical area. <pre> datacenterName.operation = '^= dal' </pre> 

List Pods in a region fulfilling capabilities. <pre> datacenterName.operation = '^= dal' capabilities.operation = 'in' capabilities.options = [ { name = data, value = [SOME_CAPABILITY, ANOTHER_CAPABILITY] } ] </pre> "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Pod"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Pod"
---

### [REST Example](#getAllObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Pod/getAllObjects'
```

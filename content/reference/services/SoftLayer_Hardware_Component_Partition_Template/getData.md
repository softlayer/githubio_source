---
title: "getData"
description: "An individual partition for a partition template. This is identical to 'partitionTemplatePartition' except this will sort unix partitions."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition_Template"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Component_Partition_Template"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Component_Partition_Template/{SoftLayer_Hardware_Component_Partition_TemplateID}/getData'
```

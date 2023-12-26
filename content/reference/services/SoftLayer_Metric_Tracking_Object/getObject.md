---
title: "getObject"
description: "getObject retrieves the SoftLayer_Metric_Tracking_Object object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Metric_Tracking_Object service. You can only tracking objects that are associated with your SoftLayer account or services. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object"
type: "reference"
layout: "method"
mainService : "SoftLayer_Metric_Tracking_Object"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Metric_Tracking_Object/{SoftLayer_Metric_Tracking_ObjectID}/getObject'
```

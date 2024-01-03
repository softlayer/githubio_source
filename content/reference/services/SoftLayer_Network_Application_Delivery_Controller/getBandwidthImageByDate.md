---
title: "getBandwidthImageByDate"
description: "Use this method when needing a bandwidth image for a single application delivery controller. It will gather the correct input parameters for the generic graphing utility based on the date ranges "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Application_Delivery_Controller"
---

# [REST Example](#getBandwidthImageByDate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBandwidthImageByDate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller/{SoftLayer_Network_Application_Delivery_ControllerID}/getBandwidthImageByDate'
```

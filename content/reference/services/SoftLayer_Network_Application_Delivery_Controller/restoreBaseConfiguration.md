---
title: "restoreBaseConfiguration"
description: "Restore an application delivery controller's base configuration state. The configuration will be set to what it was when initially provisioned. "
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

# [REST Example](#restoreBaseConfiguration-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#restoreBaseConfiguration-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller/{SoftLayer_Network_Application_Delivery_ControllerID}/restoreBaseConfiguration'
```

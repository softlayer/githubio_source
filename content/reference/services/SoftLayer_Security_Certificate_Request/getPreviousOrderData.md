---
title: "getPreviousOrderData"
description: "Returns previous SSL certificate order data. You can use this data for to place a renewal order for a completed SSL certificate. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Security_Certificate_Request"
---

### [REST Example](#getPreviousOrderData-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPreviousOrderData-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate_Request/{SoftLayer_Security_Certificate_RequestID}/getPreviousOrderData'
```

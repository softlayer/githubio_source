---
title: "getInvoice"
description: "This is the invoice associated with the upgrade request. For hourly servers or services, an invoice will not be available."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Upgrade_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Upgrade_Request"
---

### [REST Example](#getInvoice-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getInvoice-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Upgrade_Request/{SoftLayer_Product_Upgrade_RequestID}/getInvoice'
```

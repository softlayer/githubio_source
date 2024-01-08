---
title: "getChildren"
description: "An Invoice Item's child invoice items. Only parent invoice items have children. For instance, a server invoice item will have children."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Item"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Invoice_Item"
---

### [REST Example](#getChildren-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getChildren-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice_Item/{SoftLayer_Billing_Invoice_ItemID}/getChildren'
```

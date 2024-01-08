---
title: "getParent"
description: "Every item tied to a server should have a parent invoice item which is the server line item. This is how we associate items to a server."
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

### [REST Example](#getParent-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getParent-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice_Item/{SoftLayer_Billing_Invoice_ItemID}/getParent'
```

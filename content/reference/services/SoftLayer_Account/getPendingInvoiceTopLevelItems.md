---
title: "getPendingInvoiceTopLevelItems"
description: "A list of top-level invoice items that are on an account's currently pending invoice."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

### [REST Example](#getPendingInvoiceTopLevelItems-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPendingInvoiceTopLevelItems-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getPendingInvoiceTopLevelItems'
```

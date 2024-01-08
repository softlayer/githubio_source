---
title: "getPdfDetailed"
description: "Return an account's next invoice detailed portion in PDF format."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Next"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Invoice_Next"
---

### [REST Example](#getPdfDetailed-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPdfDetailed-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Invoice_Next/{SoftLayer_Billing_Invoice_NextID}/getPdfDetailed'
```

---
title: "getObject"
description: "getObject retrieves the SoftLayer_Billing_Item_Cancellation_Request object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Billing_Item_Cancellation_Request service. You can only retrieve cancellation request records that are assigned to your SoftLayer account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Cancellation_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Item_Cancellation_Request"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Cancellation_Request/{SoftLayer_Billing_Item_Cancellation_RequestID}/getObject'
```

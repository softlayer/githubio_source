---
title: "setAssociationId"
description: "Set an associated billing item to an orphan billing item. Associations allow you to tie an 'orphaned' billing item, any non-server billing item that doesn't have a parent item such as secondary IP subnets or StorageLayer accounts, to a server billing item. You may only set an association for an orphan to a server. You cannot associate a server to an orphan if the either the server or orphan billing items have a cancellation date set. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Virtual_DedicatedHost"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Item_Virtual_DedicatedHost"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Virtual_DedicatedHost/{SoftLayer_Billing_Item_Virtual_DedicatedHostID}/setAssociationId'
```

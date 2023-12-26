---
title: "cancelItem"
description: "Cancel the resource or service for a billing Item. By default the billing item will be canceled on the next bill date and reclaim of the resource will begin shortly after the cancellation. Setting the 'cancelImmediately' property to true will start the cancellation immediately if the item is eligible to be canceled immediately. 

The reason parameter could be from the list below: 
* 'No longer needed'
* 'Business closing down'
* 'Server / Upgrade Costs'
* 'Migrating to larger server'
* 'Migrating to smaller server'
* 'Migrating to a different SoftLayer datacenter'
* 'Network performance / latency'
* 'Support response / timing'
* 'Sales process / upgrades'
* 'Moving to competitor'"
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [boolean, boolean, string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Virtual_DedicatedHost/{SoftLayer_Billing_Item_Virtual_DedicatedHostID}/cancelItem'
```

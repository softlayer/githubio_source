---
title: "cancelService"
description: "Cancel the resource or service (excluding bare metal servers) for a billing Item. The billing item will be cancelled imm... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Virtual_DedicatedHost"
aliases:
    - "/reference/services/softlayer_billing_item_virtual_dedicatedhost/cancelService"
---
# [SoftLayer_Billing_Item_Virtual_DedicatedHost](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost)::cancelService


Cancel a service or resource immediately. This does not include bare metal servers. 


## Overview 
Cancel the resource or service (excluding bare metal servers) for a billing Item. The billing item will be cancelled immediately and reclaim of the resource will begin shortly. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Billing_Item_Virtual_DedicatedHostInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> <<< EOT 




---
title: "getCurrentBillingDetail"
description: "Get the billing detail for this hardware for the current billing period. This does not include bandwidth usage."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getCurrentBillingDetail"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getCurrentBillingDetail

<< EOT


## Overview 
Get the billing detail for this hardware for the current billing period. This does not include bandwidth usage. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters

### Optional Headers
* SoftLayer_Hardware_ServerObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>


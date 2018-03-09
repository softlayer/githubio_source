---
title: "getCurrentBillingDetail"
description: "Get the billing detail for this instance for the current billing period. This does not include bandwidth usage."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
---
# [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware)::getCurrentBillingDetail

Get the detail billing data for this instance's current billing period. This excludes bandwidth usage.


## Overview 
Get the billing detail for this instance for the current billing period. This does not include bandwidth usage. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_HardwareInitParameters

### Optional Headers
* SoftLayer_HardwareObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>


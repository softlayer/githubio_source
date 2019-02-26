---
title: "getCurrentBillingDetail"
description: "Get the billing detail for this hardware for the current billing period. This does not include bandwidth usage."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
aliases:
    - "/reference/services/softlayer_hardware/getCurrentBillingDetail"
---
# [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware)::getCurrentBillingDetail

<< EOT


## Overview 
Get the billing detail for this hardware for the current billing period. This does not include bandwidth usage. 

-----

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
* <a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>





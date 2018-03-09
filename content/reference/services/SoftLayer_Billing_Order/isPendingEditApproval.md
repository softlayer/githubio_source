---
title: "isPendingEditApproval"
description: "When an order has been modified, it will contain a status indicating so. This method checks that status and also verifie... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
---
# [SoftLayer_Billing_Order](/reference/services/SoftLayer_Billing_Order)::isPendingEditApproval

Determine if the existing order is pending edit approval


## Overview 
When an order has been modified, it will contain a status indicating so. This method checks that status and also verifies that the active user's account is the same as the account on the order. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Billing_OrderInitParameters

### Optional Headers

### Return Values
boolean


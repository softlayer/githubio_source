---
title: "getPendingInvoiceTotalOneTimeAmount"
description: "Retrieve the total one-time charges for an account's pending invoice, if one exists. In other words, it is the sum of on... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# SoftLayer_Account::getPendingInvoiceTotalOneTimeAmount
## Overview 
Retrieve the total one-time charges for an account's pending invoice, if one exists. In other words, it is the sum of one-time charges, setup fees, and labor fees. It does not include taxes.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_AccountObjectMask
* SoftLayer_AccountObjectFilter
* SoftLayer_ObjectMask

### Return Values
decimal


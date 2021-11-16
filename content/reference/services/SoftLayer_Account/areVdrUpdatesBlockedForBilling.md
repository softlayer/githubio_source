---
title: "areVdrUpdatesBlockedForBilling"
description: "This method indicates whether or not Bandwidth Pooling updates are blocked for the account so the billing cycle can run.... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/areVdrUpdatesBlockedForBilling"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::areVdrUpdatesBlockedForBilling


This method returns true if Bandwidth Pooling updates are blocked so billing can run for this account.


## Overview 
This method indicates whether or not Bandwidth Pooling updates are blocked for the account so the billing cycle can run.  Generally, accounts are restricted from moving servers in or out of Bandwidth Pools from 12:00 CST on the day prior to billing, until the billing batch completes, sometime after midnight the day of actual billing for the account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate


### Return Values
* boolean





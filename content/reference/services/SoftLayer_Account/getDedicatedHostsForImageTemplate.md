---
title: "getDedicatedHostsForImageTemplate"
description: "This returns a collection of dedicated hosts that are valid for a given image template."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getDedicatedHostsForImageTemplate"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getDedicatedHostsForImageTemplate

Get a collection of dedicated hosts that are valid for a given image template. 


## Overview 
This returns a collection of dedicated hosts that are valid for a given image template. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|imageTemplateId| integer| A [[SoftLayer_Virtual_Guest_Block_Device_Template_Group]] id to get dedicated hosts for|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_AccountObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost[] </a>





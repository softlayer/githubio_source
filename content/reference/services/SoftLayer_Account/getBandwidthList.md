---
title: "getBandwidthList"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getBandwidthList"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getBandwidthList




## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|networkType| string| Specify either the public or private network|
|direction| string| Specify either in or out usage|
|startDate| string| Beginning of cycle to sum usage|
|endDate| string| Beginning of cycle to sum usage|
|serverIds| array of integers| Integer array of specific server IDs|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Bandwidth_Usage'>SoftLayer_Container_Bandwidth_Usage[] </a>





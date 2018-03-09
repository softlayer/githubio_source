---
title: "getAvailableHourlyInstanceLimit"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Group"
---
# [SoftLayer_Scale_Group](/reference/services/SoftLayer_Scale_Group)::getAvailableHourlyInstanceLimit

This returns the number of hourly instances an account can add from this point. It is essentially the same as [[SoftLayer_Account/hourlyInstanceLimit|hourlyInstanceLimit]] minus existing hourly instances and ones spoken for as part of a scaling group (as determined by the group's maximum). This number can be used to help determine a maximum member count for a new group to ensure it won't go over the account limit. This can return a negative value if the current hourly instance count combined with the unused-but-possible count (based on other scale group maximums) is over the limit. 


## Overview 


### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers

### Return Values
integer


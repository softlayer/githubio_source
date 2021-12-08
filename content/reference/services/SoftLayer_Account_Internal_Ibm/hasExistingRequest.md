---
title: "hasExistingRequest"
description: "Checks for an existing request which would block an IBMer from submitting a new request. Such a request could be denied,... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Internal_Ibm"
aliases:
    - "/reference/services/softlayer_account_internal_ibm/hasExistingRequest"
---
# [SoftLayer_Account_Internal_Ibm](/reference/services/SoftLayer_Account_Internal_Ibm)::hasExistingRequest


Checks for an existing request which would block an IBMer application


## Overview 
Checks for an existing request which would block an IBMer from submitting a new request. Such a request could be denied, approved, or awaiting manager action. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|employeeUid| string| |
|managerUid| string| |


### Required Headers
* authenticate


### Return Values
* boolean





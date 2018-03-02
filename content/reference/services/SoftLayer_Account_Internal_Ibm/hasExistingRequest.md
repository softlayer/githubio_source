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
---
# SoftLayer_Account_Internal_Ibm::hasExistingRequest
## Overview 
Checks for an existing request which would block an IBMer from submitting a new request. Such a request could be denied, approved, or awaiting manager action. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|employeeUid| string| |
|managerUid| string| |


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean


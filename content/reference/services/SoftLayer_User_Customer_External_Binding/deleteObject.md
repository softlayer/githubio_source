---
title: "deleteObject"
description: "Delete an external authentication binding.  If the external binding currently has an active billing item associated you... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding"
---
# SoftLayer_User_Customer_External_Binding::deleteObject
## Overview 
Delete an external authentication binding.  If the external binding currently has an active billing item associated you will be prevented from deleting the binding.  The alternative method to remove an external authentication binding is to use the service cancellation form. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_User_Customer_External_BindingInitParameters

### Optional Headers

### Return Values
boolean

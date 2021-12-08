---
title: "deleteObject"
description: "Delete a VeriSign external binding.  The only VeriSign external binding that can be deleted through this method is the f... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Verisign"
aliases:
    - "/reference/services/softlayer_user_customer_external_binding_verisign/deleteObject"
---
# [SoftLayer_User_Customer_External_Binding_Verisign](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign)::deleteObject


Delete a VeriSign external binding.


## Overview 
Delete a VeriSign external binding.  The only VeriSign external binding that can be deleted through this method is the free VeriSign external binding for the master user of a SoftLayer account. All other external bindings must be canceled using the SoftLayer service cancellation form. 

When a VeriSign external binding is deleted the credential is deactivated in VeriSign's system for use on the SoftLayer site and the $0 billing item associated with the free VeriSign external binding is cancelled. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_User_Customer_External_Binding_VerisignInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throw the error "You do not have permission 




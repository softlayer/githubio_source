---
title: "getActiveExternalAuthenticationVendors"
description: "The getActiveExternalAuthenticationVendors method will return a list of available external vendors that a SoftLayer user... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# SoftLayer_User_Customer_OpenIdConnect::getActiveExternalAuthenticationVendors
## Overview 
The getActiveExternalAuthenticationVendors method will return a list of available external vendors that a SoftLayer user can authenticate against.  The list will only contain vendors for which the user has at least one active external binding. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_User_Customer_External_Binding_Vendor'>SoftLayer_Container_User_Customer_External_Binding_Vendor[] </a>

---
title: "getActiveExternalAuthenticationVendors"
description: "The getActiveExternalAuthenticationVendors method will return a list of available external vendors that a SoftLayer user... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/getActiveExternalAuthenticationVendors"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::getActiveExternalAuthenticationVendors


Get a list of active external authentication vendors for a SoftLayer user.


## Overview 
The getActiveExternalAuthenticationVendors method will return a list of available external vendors that a SoftLayer user can authenticate against.  The list will only contain vendors for which the user has at least one active external binding. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_User_Customer_External_Binding_Vendor'>SoftLayer_Container_User_Customer_External_Binding_Vendor[] </a>





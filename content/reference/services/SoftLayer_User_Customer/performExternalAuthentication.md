---
title: "performExternalAuthentication"
description: "The perform external authentication method will authenticate the given external authentication container with an externa... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/performExternalAuthentication"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::performExternalAuthentication

Perform an external authentication using the given authentication container.


## Overview 
The perform external authentication method will authenticate the given external authentication container with an external vendor.  The authentication container and its contents will be verified before an attempt is made to authenticate the contents of the container with an external vendor. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|authenticationContainer| <a href='/reference/datatypes/SoftLayer_Container_User_Customer_External_Binding'>SoftLayer_Container_User_Customer_External_Binding </a>| The authentication container with the external authentication information.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_User_Customer_Portal_Token'>SoftLayer_Container_User_Customer_Portal_Token </a>


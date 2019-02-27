---
title: "setDefaultAccount"
description: "An OpenIdConnect identity, for example an IBMid, can be linked or mapped to one or more individual SoftLayer users, but... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/setDefaultAccount"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::setDefaultAccount

Sets the default account for the OpenIdConnect identity that is linked to the current SoftLayer user identity.


## Overview 
An OpenIdConnect identity, for example an IBMid, can be linked or mapped to one or more individual SoftLayer users, but no more than one per account. If an OpenIdConnect identity is mapped to multiple accounts in this manner, one such account should be identified as the default account for that identity. Invoke this only on IBMid-authenticated users. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| A value representing the OpenID Connect provider type. Currently "IBMid" is the only supported provider.|
|accountId| integer| The Softlayer account to set as default.|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters


### Optional Headers
* SoftLayer_User_CustomerObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>





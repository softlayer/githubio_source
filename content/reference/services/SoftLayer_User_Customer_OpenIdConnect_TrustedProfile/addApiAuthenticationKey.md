---
title: "addApiAuthenticationKey"
description: "Create a user's API authentication key, allowing that user access to query the SoftLayer API. addApiAuthenticationKey()... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/addApiAuthenticationKey"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::addApiAuthenticationKey

Create a user's API authentication key.


## Overview 
Create a user's API authentication key, allowing that user access to query the SoftLayer API. addApiAuthenticationKey() returns the user's new API key. Each portal user is allowed only one API key. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileInitParameters


### Return Values
* string


### Associated Methods

*  [SoftLayer_User_Customer::removeApiAuthenticationKey](/reference/services/SoftLayer_User_Customer/removeApiAuthenticationKey )



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception "Generating an API key for a user in PENDING status is disallowed." if the given user is in PENDING status. 

* SoftLayer_Exception_Public 

> Throws the exception "Each user can only have a single API key." if the given user already has an API key defined. 




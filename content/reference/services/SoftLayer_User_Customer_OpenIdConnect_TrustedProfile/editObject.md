---
title: "editObject"
description: "Account master users and sub-users who have the User Manage permission in the SoftLayer customer portal can update other... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/editObject"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::editObject

Update a user's information.


## Overview 
Account master users and sub-users who have the User Manage permission in the SoftLayer customer portal can update other user's information. Use editObject() if you wish to edit a single user account. Users who do not have the User Manage permission can only update their own information. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile'>SoftLayer_User_Customer_OpenIdConnect_TrustedProfile </a>| A skeleton SoftLayer_User_Customer_OpenIdConnect_TrustedProfile object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::editObjects](/reference/services/SoftLayer_User_Customer/editObjects )





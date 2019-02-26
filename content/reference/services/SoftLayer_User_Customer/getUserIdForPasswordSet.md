---
title: "getUserIdForPasswordSet"
description: "Retrieve a user object using a password token. When a new user is created or when a user has requested a password change... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/getUserIdForPasswordSet"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::getUserIdForPasswordSet

Retrieve a user object using a password request key


## Overview 
Retrieve a user object using a password token. When a new user is created or when a user has requested a password change using initiatePortalPasswordChange, they will have received an email that contains a url with a token.  That token is used as the parameter for getUserIdForPasswordSet. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|key| string| A password recovery hash key retrieved from an email.|


### Required Headers


### Return Values
* integer


### Associated Methods

*  [SoftLayer_User_Customer::initiatePortalPasswordChange](/reference/services/SoftLayer_User_Customer/initiatePortalPasswordChange )
*  [SoftLayer_User_Customer::getRequirementsForPasswordSet](/reference/services/SoftLayer_User_Customer/getRequirementsForPasswordSet )
*  [SoftLayer_User_Customer::processPasswordSetRequest](/reference/services/SoftLayer_User_Customer/processPasswordSetRequest )
*  [SoftLayer_User_Customer::checkPhoneFactorAuthenticationForPasswordSet](/reference/services/SoftLayer_User_Customer/checkPhoneFactorAuthenticationForPasswordSet )



### Error Handling

* SoftLayer_Exception_Public 

> <<< EOT 




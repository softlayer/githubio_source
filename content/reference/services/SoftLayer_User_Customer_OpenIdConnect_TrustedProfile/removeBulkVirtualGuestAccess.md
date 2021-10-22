---
title: "removeBulkVirtualGuestAccess"
description: "Remove multiple CloudLayer Computing Instances from a portal user's access list. A user's CloudLayer Computing Instance... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/removeBulkVirtualGuestAccess"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::removeBulkVirtualGuestAccess

Remove multiple CloudLayer Computing Instances from a portal user's access list.


## Overview 
Remove multiple CloudLayer Computing Instances from a portal user's access list. A user's CloudLayer Computing Instance access list controls which of an account's CloudLayer Computing Instance objects a user has access to in the SoftLayer customer portal and API. CloudLayer Computing Instances do not exist in the SoftLayer portal and returns "not found" exceptions in the API if the user doesn't have access to it. If a user does not has access to the CloudLayer Computing Instance you're attempting remove add then removeBulkVirtualGuestAccess() returns true. 

Users can assign CloudLayer Computing Instance access to their child users, but not to themselves. An account's master has access to all CloudLayer Computing Instances on their customer account and can set hardware access for any of the other users on their account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|virtualGuestIds| array of integers| The internal identifiers of the CloudLayer Computing Instances you wish to remove access to.|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::addVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/addVirtualGuestAccess )
*  [SoftLayer_User_Customer::addBulkVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/addBulkVirtualGuestAccess )
*  [SoftLayer_User_Customer::removeVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/removeVirtualGuestAccess )



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You may not grant or deny Master User device access." when trying to remove virtual guest access to a master user. 

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You may not grant or deny yourself device access." when trying to remove virtual guest access to the user making the call to the SoftLayer API. 

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You may not grant or deny device access to other users." when trying to remove virtual guest access the user making the API call is not their account's master user or does not have the "USER_MANAGE" portal permission. 

* SoftLayer_Exception_Public 

> Throws the exception "Please specify a valid CloudLayer Computing Instance id." if the given CloudLayer Computing Instance id is not a valid id. 

* SoftLayer_Exception_Public 

> Throws the exception "Unable to remove user CloudLayer Computing Instance access." if the API was unable to remove CloudLayer Computing Instance access from the given portal user. 




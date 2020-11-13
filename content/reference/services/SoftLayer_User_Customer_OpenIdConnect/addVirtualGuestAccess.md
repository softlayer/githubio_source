---
title: "addVirtualGuestAccess"
description: "Add a CloudLayer Computing Instance to a portal user's access list. A user's CloudLayer Computing Instance access list c... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/addVirtualGuestAccess"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::addVirtualGuestAccess

Add a CloudLayer Computing Instance to a portal user's access list.


## Overview 
Add a CloudLayer Computing Instance to a portal user's access list. A user's CloudLayer Computing Instance access list controls which of an account's CloudLayer Computing Instance objects a user has access to in the SoftLayer customer portal and API. CloudLayer Computing Instances do not exist in the SoftLayer portal and returns "not found" exceptions in the API if the user doesn't have access to it. If a user already has access to the CloudLayer Computing Instance you're attempting to add then addVirtualGuestAccess() returns true. 

Users can assign CloudLayer Computing Instance access to their child users, but not to themselves. An account's master has access to all CloudLayer Computing Instances on their customer account and can set CloudLayer Computing Instance access for any of the other users on their account. 

Only the USER_MANAGE permission is required to execute this. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|virtualGuestId| integer| The identifier of the Virtual Server to add to a user's access list.|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::addBulkVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/addBulkVirtualGuestAccess )
*  [SoftLayer_User_Customer::removeVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/removeVirtualGuestAccess )
*  [SoftLayer_User_Customer::removeBulkVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/removeBulkVirtualGuestAccess )



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You may not grant or deny Master User device access." when trying to add virtual guest access to a master user. 

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You may not grant or deny yourself device access." when trying to add virtual guest access to the user making the call to the SoftLayer API. 

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You may not grant or deny device access to other users." when trying to add virtual guest access the user making the API call is not their account's master user or does not have the "USER_MANAGE" portal permission. 

* SoftLayer_Exception_Public 

> Throws the exception "You may not add Virtual Server permissions that the parent does not possess to this account." when trying to add Virtual Server access to the user and the parent user does not possess that access to that Virtual Server. 

* SoftLayer_Exception_Public 

> Throws the exception "Please specify a valid Virtual Server id." if the given Virtual Server id is not a valid id. 

* SoftLayer_Exception_Public 

> Throws the exception "Unable to add user Virtual Server access." if the API was unable to assign Virtual Server access to the given portal user. 




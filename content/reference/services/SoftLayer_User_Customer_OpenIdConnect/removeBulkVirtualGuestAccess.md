---
title: "removeBulkVirtualGuestAccess"
description: "Remove multiple CloudLayer Computing Instances from a portal user's access list. A user's CloudLayer Computing Instance... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/removeBulkVirtualGuestAccess"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::removeBulkVirtualGuestAccess

Remove multiple CloudLayer Computing Instances from a portal user's access list.


## Overview 
Remove multiple CloudLayer Computing Instances from a portal user's access list. A user's CloudLayer Computing Instance access list controls which of an account's CloudLayer Computing Instance objects a user has access to in the SoftLayer customer portal and API. CloudLayer Computing Instances do not exist in the SoftLayer portal and returns "not found" exceptions in the API if the user doesn't have access to it. If a user does not has access to the CloudLayer Computing Instance you're attempting remove add then removeBulkVirtualGuestAccess() returns true. 

Users can assign CloudLayer Computing Instance access to their child users, but not to themselves. An account's master has access to all CloudLayer Computing Instances on their customer account and can set hardware access for any of the other users on their account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|virtualGuestIds| array of integers| The internal identifiers of the CloudLayer Computing Instances you wish to remove access to.|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::addVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/addVirtualGuestAccess )
*  [SoftLayer_User_Customer::addBulkVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/addBulkVirtualGuestAccess )
*  [SoftLayer_User_Customer::removeVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/removeVirtualGuestAccess )


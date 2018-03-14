---
title: "addBulkVirtualGuestAccess"
description: "Add multiple CloudLayer Computing Instances to a portal user's access list. A user's CloudLayer Computing Instance acces... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/addBulkVirtualGuestAccess"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::addBulkVirtualGuestAccess

Add multiple CloudLayer Computing Instances to a portal user's access list.


## Overview 
Add multiple CloudLayer Computing Instances to a portal user's access list. A user's CloudLayer Computing Instance access list controls which of an account's CloudLayer Computing Instance objects a user has access to in the SoftLayer customer portal and API. CloudLayer Computing Instances do not exist in the SoftLayer portal and returns "not found" exceptions in the API if the user doesn't have access to it. addBulkVirtualGuestAccess() does not attempt to add CloudLayer Computing Instance access if the given user already has access to that CloudLayer Computing Instance object. 

Users can assign CloudLayer Computing Instance access to their child users, but not to themselves. An account's master has access to all CloudLayer Computing Instances on their customer account and can set CloudLayer Computing Instance access for any of the other users on their account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|virtualGuestIds| array of integers| The internal identifiers of the CloudLayer Computing Instances you wish to add access to.|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::addVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/addVirtualGuestAccess )
*  [SoftLayer_User_Customer::removeVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/removeVirtualGuestAccess )
*  [SoftLayer_User_Customer::removeBulkVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/removeBulkVirtualGuestAccess )


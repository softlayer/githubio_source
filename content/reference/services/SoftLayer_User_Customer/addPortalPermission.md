---
title: "addPortalPermission"
description: "Add a permission to a portal user's permission set. [[Permissions]] control which features in the SoftLayer customer por... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/addPortalPermission"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::addPortalPermission

Add a permission to a portal user's permission set.


## Overview 
Add a permission to a portal user's permission set. [[Permissions]] control which features in the SoftLayer customer portal and API a user may use. If the user already has the permission you're attempting to add then addPortalPermission() returns true. 

Users can assign permissions to their child users, but not to themselves. An account's master has all portal permissions and can set permissions for any of the other users on their account. 

Use the [[SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects]] method to retrieve a list of all permissions available in the SoftLayer customer portal and API. Permissions are added based on the keyName property of the permission parameter. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|permission| <a href='/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission'>SoftLayer_User_Customer_CustomerPermission_Permission </a>| The permission you wish to add to the given user.|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::addBulkPortalPermission](/reference/services/SoftLayer_User_Customer/addBulkPortalPermission )
*  [SoftLayer_User_Customer::removePortalPermission](/reference/services/SoftLayer_User_Customer/removePortalPermission )
*  [SoftLayer_User_Customer::removeBulkPortalPermission](/reference/services/SoftLayer_User_Customer/removeBulkPortalPermission )


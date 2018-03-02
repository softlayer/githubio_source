---
title: "removeBulkPortalPermission"
description: "Remove multiple permissions from a portal user's permission set. [[Permissions]] control which features in the SoftLayer... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer::removeBulkPortalPermission
## Overview 
Remove multiple permissions from a portal user's permission set. [[Permissions]] control which features in the SoftLayer customer portal and API a user may use. Removing a user's permission will affect that user's portal and API access. removePortalPermission() does not attempt to remove permissions that are not assigned to the user. 

Users can assign permissions to their child users, but not to themselves. An account's master has all portal permissions and can set permissions for any of the other users on their account. 

Use the [[SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects]] method to retrieve a list of all permissions available in the SoftLayer customer portal and API. Permissions are removed based on the keyName property of the permission objects within the permissions parameter. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|permissions| <a href='/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission'>SoftLayer_User_Customer_CustomerPermission_Permission[] </a>| A collection of permissions to remove from this user.|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::addPortalPermission](/reference/services/SoftLayer_User_Customer/addPortalPermission )
*  [SoftLayer_User_Customer::addBulkPortalPermission](/reference/services/SoftLayer_User_Customer/addBulkPortalPermission )
*  [SoftLayer_User_Customer::removeBulkPortalPermission](/reference/services/SoftLayer_User_Customer/removeBulkPortalPermission )


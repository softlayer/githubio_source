---
title: "removePortalPermission"
description: "Remove (revoke) a permission from a portal user's permission set. [[Permissions]] control which features in the SoftLaye... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/removePortalPermission"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::removePortalPermission

Remove a permission from a portal user's permission set.


## Overview 
Remove (revoke) a permission from a portal user's permission set. [[Permissions]] control which features in the SoftLayer customer portal and API a user may use. Removing a user's permission will affect that user's portal and API access. If the user does not have the permission you're attempting to remove then removePortalPermission() returns true. 

Users can assign permissions to their child users, but not to themselves. An account's master has all portal permissions and can set permissions for any of the other users on their account. 

If the cascadePermissionsFlag is set to true, then removing the permission from a user will cascade down the child hierarchy and remove the permission from this user and all child users who also have the permission. 

If the cascadePermissionsFlag is not set or is set to false and the user has children users who have the permission, then an exception will be thrown, and the permission will not be removed from this user. 

Use the [[SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects]] method to retrieve a list of all permissions available in the SoftLayer customer portal and API. Permissions are removed based on the keyName property of the permission parameter. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|permission| <a href='/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission'>SoftLayer_User_Customer_CustomerPermission_Permission </a>| The permission you wish to add to the given user.|
|cascadePermissionsFlag| boolean| |


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::addPortalPermission](/reference/services/SoftLayer_User_Customer/addPortalPermission )
*  [SoftLayer_User_Customer::addBulkPortalPermission](/reference/services/SoftLayer_User_Customer/addBulkPortalPermission )
*  [SoftLayer_User_Customer::removeBulkPortalPermission](/reference/services/SoftLayer_User_Customer/removeBulkPortalPermission )


---
title: "removeBulkPortalPermission"
description: "Remove (revoke) multiple permissions from a portal user's permission set. [SoftLayer_User_Customer_CustomerPermission_Pe... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/removeBulkPortalPermission"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::removeBulkPortalPermission

Remove multiple permissions from a portal user's permission set.


## Overview 
Remove (revoke) multiple permissions from a portal user's permission set. [SoftLayer_User_Customer_CustomerPermission_Permission]({{<ref "reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission">}}) control which features in the SoftLayer customer portal and API a user may use. Removing a user's permission will affect that user's portal and API access. removePortalPermission() does not attempt to remove permissions that are not assigned to the user. 

Users can grant or revoke permissions to their child users, but not to themselves. An account's master has all portal permissions and can grant permissions for any of the other users on their account. 

If the cascadePermissionsFlag is set to true, then removing the permissions from a user will cascade down the child hierarchy and remove the permissions from this user along with all child users who also have the permission. 

If the cascadePermissionsFlag is not provided or is set to false and the user has children users who have the permission, then an exception will be thrown, and the permission will not be removed from this user. 

Use the [SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects]({{<ref "reference/services/SoftLayer_User_Customer_CustomerPermission_Permission/getAllObjects">}}) method to retrieve a list of all permissions available in the SoftLayer customer portal and API. Permissions are removed based on the keyName property of the permission objects within the permissions parameter. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|permissions| <a href='/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission'>SoftLayer_User_Customer_CustomerPermission_Permission[] </a>| A collection of permissions to remove from this user.|
|cascadePermissionsFlag| boolean| |


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::addPortalPermission](/reference/services/SoftLayer_User_Customer/addPortalPermission )
*  [SoftLayer_User_Customer::addBulkPortalPermission](/reference/services/SoftLayer_User_Customer/addBulkPortalPermission )
*  [SoftLayer_User_Customer::removeBulkPortalPermission](/reference/services/SoftLayer_User_Customer/removeBulkPortalPermission )



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception "You may not remove permissions from your account." when trying to remove permissions from the user making calling the SoftLayer API. 

* SoftLayer_Exception_Public 

> Throws the exception "Please specify a permission key name." if the keyName property of the permission parameter is empty. 

* SoftLayer_Exception_Public 

> Throws the exception "Unable to locate a permission with the key name {key name}." when trying to remove an unknown permission from a user. 

* SoftLayer_Exception_Public 

> Throws the exception "Unable to remove user permission {key name}." if the API was unable to remove the given permission from the given portal user. 




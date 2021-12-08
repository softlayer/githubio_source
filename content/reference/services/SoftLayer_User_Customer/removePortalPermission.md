---
title: "removePortalPermission"
description: "Remove (revoke) a permission from a portal user's permission set. [SoftLayer_User_Customer_CustomerPermission_Permission... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/removePortalPermission"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::removePortalPermission


Remove a permission from a portal user's permission set.


## Overview 
Remove (revoke) a permission from a portal user's permission set. [SoftLayer_User_Customer_CustomerPermission_Permission]({{<ref "reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission">}}) control which features in the SoftLayer customer portal and API a user may use. Removing a user's permission will affect that user's portal and API access. If the user does not have the permission you're attempting to remove then removePortalPermission() returns true. 

Users can assign permissions to their child users, but not to themselves. An account's master has all portal permissions and can set permissions for any of the other users on their account. 

If the cascadePermissionsFlag is set to true, then removing the permission from a user will cascade down the child hierarchy and remove the permission from this user and all child users who also have the permission. 

If the cascadePermissionsFlag is not set or is set to false and the user has children users who have the permission, then an exception will be thrown, and the permission will not be removed from this user. 

Use the [SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects]({{<ref "reference/services/SoftLayer_User_Customer_CustomerPermission_Permission/getAllObjects">}}) method to retrieve a list of all permissions available in the SoftLayer customer portal and API. Permissions are removed based on the keyName property of the permission parameter. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|permission| <a href='/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission'>SoftLayer_User_Customer_CustomerPermission_Permission </a>| The permission you wish to add to the given user.|
|cascadePermissionsFlag| boolean| |


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters


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

> Throws the exception "You may not remove permissions from this account." the user making the API call is not their account's master user or does not have the "Add New User" portal permission. 

* SoftLayer_Exception_Public 

> Throws the exception "Please specify a permission key name." if the keyName property of the permission parameter is empty. 

* SoftLayer_Exception_Public 

> Throws the exception "Unable to locate a permission with the key name {key name}." when trying to remove an unknown permission from a user. 

* SoftLayer_Exception_Public 

> Throws the exception "Unable to remove user permission {key name}." if the API was unable to remove the given permission from the given portal user. 




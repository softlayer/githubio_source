---
title: "removePortalPermission"
description: "Remove (revoke) a permission from a portal user's permission set. [SoftLayer_User_Customer_CustomerPermission_Permission](/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission) control which features in the SoftLayer customer portal and API a user may use. Removing a user's permission will affect that user's portal and API access. If the user does not have the permission you're attempting to remove then removePortalPermission() returns true. 

Users can assign permissions to their child users, but not to themselves. An account's master has all portal permissions and can set permissions for any of the other users on their account. 

If the cascadePermissionsFlag is set to true, then removing the permission from a user will cascade down the child hierarchy and remove the permission from this user and all child users who also have the permission. 

If the cascadePermissionsFlag is not set or is set to false and the user has children users who have the permission, then an exception will be thrown, and the permission will not be removed from this user. 

Use the [SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects](/reference/datatypes/$1/#$2) method to retrieve a list of all permissions available in the SoftLayer customer portal and API. Permissions are removed based on the keyName property of the permission parameter. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Customer_CustomerPermission_Permission, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/{SoftLayer_User_Customer_OpenIdConnect_TrustedProfileID}/removePortalPermission'
```

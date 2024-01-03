---
title: "addBulkPortalPermission"
description: "Add multiple permissions to a portal user's permission set. [SoftLayer_User_Customer_CustomerPermission_Permission](/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission) control which features in the SoftLayer customer portal and API a user may use. addBulkPortalPermission() does not attempt to add permissions already assigned to the user. 

Users can assign permissions to their child users, but not to themselves. An account's master has all portal permissions and can set permissions for any of the other users on their account. 

Use the [SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects](/reference/datatypes/$1/#$2) method to retrieve a list of all permissions available in the SoftLayer customer portal and API. Permissions are removed based on the keyName property of the permission objects within the permissions parameter. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect"
---

# [REST Example](#addBulkPortalPermission-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addBulkPortalPermission-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Customer_CustomerPermission_Permission]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/addBulkPortalPermission'
```

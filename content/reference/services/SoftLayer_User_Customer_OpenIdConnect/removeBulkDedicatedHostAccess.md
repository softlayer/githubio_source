---
title: "removeBulkDedicatedHostAccess"
description: "Revokes access for the user to one or more dedicated host devices.  The user will only be allowed to see and access devices in both the portal and the API to which they have been granted access.  If the user's account has devices to which the user has not been granted access or the access has been revoked, then 'not found' exceptions are thrown if the user attempts to access any of these devices. 

Users can assign device access to their child users, but not to themselves. An account's master has access to all devices on their customer account and can set dedicated host access for any of the other users on their account. 

If the user has full dedicatedHost access, then it will provide access to 'ALL but passed in' dedicatedHost ids. "
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

### [REST Example](#removeBulkDedicatedHostAccess-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeBulkDedicatedHostAccess-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/removeBulkDedicatedHostAccess'
```

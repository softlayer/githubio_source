---
title: "removeAllVirtualAccessForThisUser"
description: "Remove all cloud computing instances from a portal user's instance access list. A user's instance access list controls which of an account's computing instance objects a user has access to in the SoftLayer customer portal and API. If the current user does not have administrative privileges over this user, an inadequate permissions exception will get thrown. 

Users can call this function on child users, but not to themselves. An account's master has access to all users permissions on their account. "
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

### [REST Example](#removeAllVirtualAccessForThisUser-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeAllVirtualAccessForThisUser-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/removeAllVirtualAccessForThisUser'
```

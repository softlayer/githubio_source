---
title: "removeAllDedicatedHostAccessForThisUser"
description: "Revoke access to all dedicated hosts on the account for this user. The user will only be allowed to see and access devices in both the portal and the API to which they have been granted access.  If the user's account has devices to which the user has not been granted access or the access has been revoked, then 'not found' exceptions are thrown if the user attempts to access any of these devices. If the current user does not have administrative privileges over this user, an inadequate permissions exception will get thrown. 

Users can call this function on child users, but not to themselves. An account's master has access to all users permissions on their account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "removeAllDedicatedHostAccessForThisUser"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer"
---

---
title: "removeBulkHardwareAccess"
description: "Remove multiple hardware from a portal user's hardware access list. A user's hardware access list controls which of an account's hardware objects a user has access to in the SoftLayer customer portal and API. Hardware does not exist in the SoftLayer portal and returns 'not found' exceptions in the API if the user doesn't have access to it. If a user does not has access to the hardware you're attempting to remove then removeBulkHardwareAccess() returns true. 

Users can assign hardware access to their child users, but not to themselves. An account's master has access to all hardware on their customer account and can set hardware access for any of the other users on their account. 

If the user has full hardware access, then it will provide access to 'ALL but passed in' hardware ids. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/removeBulkHardwareAccess'
```

---
title: "getDefaultAccount"
description: "This API gets the account associated with the default user for the OpenIdConnect identity that is linked to the current active SoftLayer user identity. When a single active user is found for that IAMid, it becomes the default user and the associated account is returned. When multiple default users are found only the first is preserved and the associated account is returned (remaining defaults see their default flag unset). If the current SoftLayer user identity isn't linked to any OpenIdConnect identity, or if none of the linked users were found as defaults, the API returns null. Invoke this only on IAMid-authenticated users. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "getDefaultAccount"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect"
---

---
title: "silentlyMigrateUserOpenIdConnect"
description: "As master user, calling this api for the IBMid provider type when there is an existing IBMid for the email on the SL acc... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/silentlyMigrateUserOpenIdConnect"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::silentlyMigrateUserOpenIdConnect

This api is used to migrate a user to IBMid without sending an invitation.


## Overview 
As master user, calling this api for the IBMid provider type when there is an existing IBMid for the email on the SL account will silently (without sending an invitation email) create a link for the IBMid. NOTE: If the SoftLayer user is already linked to IBMid, this call will fail. If the IBMid specified by the email of this user, is already used in a link to another user in this account, this call will fail. If there is already an open invitation from this SoftLayer user to this or any IBMid, this call will fail. If there is already an open invitation from some other SoftLayer user in this account to this IBMid, then this call will fail. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| The provider type|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters

### Optional Headers

### Return Values
boolean


---
title: "getPortalLoginToken"
description: "Attempt to authenticate a username and password to the SoftLayer customer portal. Many portal user accounts are configur... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::getPortalLoginToken

Authenticate a user for the SoftLayer customer portal


## Overview 
Attempt to authenticate a username and password to the SoftLayer customer portal. Many portal user accounts are configured to require answering a security question on login. In this case getPortalLoginToken() also verifies the given security question ID and answer. If authentication is successful then the API returns a token containing the ID of the authenticated user and a hash key used by the SoftLayer customer portal to maintain authentication. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| The username you wish to authenticate to the SoftLayer customer portal with.|
|password| string| Your SoftLayer customer portal user's portal password.|
|securityQuestionId| integer| A security question you wish to answer when authenticating to the SoftLayer customer portal. This parameter isn't required if no security questions are set on your portal account or if your account is configured to not require answering a security account upon login.|
|securityQuestionAnswer| string| The answer to your security question.|


### Required Headers

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_User_Customer_Portal_Token'>SoftLayer_Container_User_Customer_Portal_Token </a>


---
title: "getPortalLoginTokenOpenIdConnect"
description: "Attempt to authenticate a supplied OpenIdConnect access token to the SoftLayer customer portal. If authentication is suc... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# SoftLayer_User_Customer_OpenIdConnect::getPortalLoginTokenOpenIdConnect
## Overview 
Attempt to authenticate a supplied OpenIdConnect access token to the SoftLayer customer portal. If authentication is successful then the API returns a token containing the ID of the authenticated user and a hash key used by the SoftLayer customer portal to maintain authentication. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| A value representing the OpenID Connect provider type. Currently "IBMid" is the only supported provider.|
|accessToken| string| The OpenID Connect access token which provides temporary access to a resource by the|
|accountId| integer| The preferred Softlayer account to query, if not provided a default will be used.|
|securityQuestionId| integer| A security question you wish to answer when authenticating to the SoftLayer customer portal. This parameter isn't required if no security questions are set on your portal account or if your account is configured to not require answering a security account upon login.|
|securityQuestionAnswer| string| The answer to your security question.|


### Required Headers

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_User_Customer_Portal_Token'>SoftLayer_Container_User_Customer_Portal_Token </a>


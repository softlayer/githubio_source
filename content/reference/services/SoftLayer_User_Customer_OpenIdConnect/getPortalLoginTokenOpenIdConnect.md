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
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/getPortalLoginTokenOpenIdConnect"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::getPortalLoginTokenOpenIdConnect

<div class="deprecated"><span class="deprecation-label">Deprecated </span></div>

Authenticate a user for the SoftLayer customer portal via an openIdConnect provider.


## Overview 
Attempt to authenticate a supplied OpenIdConnect access token to the SoftLayer customer portal. If authentication is successful then the API returns a token containing the ID of the authenticated user and a hash key used by the SoftLayer customer portal to maintain authentication. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| A value representing the OpenID Connect provider type.|
|accessToken| string| The OpenID Connect access token which provides temporary access to a resource by the|
|accountId| integer| The preferred Softlayer account to query, if not provided a default will be used.|
|securityQuestionId| integer| A security question you wish to answer when authenticating to the SoftLayer customer portal. This parameter isn't required if no security questions are set on your portal account or if your account is configured to not require answering a security account upon login.|
|securityQuestionAnswer| string| The answer to your security question.|


### Required Headers


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_User_Customer_Portal_Token'>SoftLayer_Container_User_Customer_Portal_Token </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Invalid answer provided for security question." if the given security question and answer are invalid and the user is required to answer security questions on portal login. 




---
title: "getPortalLoginToken"
description: "Attempt to authenticate a username and password to the SoftLayer customer portal. Many portal user accounts are configur... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/getPortalLoginToken"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::getPortalLoginToken


Authenticate a user for the SoftLayer customer portal


## Overview 
Attempt to authenticate a username and password to the SoftLayer customer portal. Many portal user accounts are configured to require answering a security question on login. In this case getPortalLoginToken() also verifies the given security question ID and answer. If authentication is successful then the API returns a token containing the ID of the authenticated user and a hash key used by the SoftLayer customer portal to maintain authentication. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| The username you wish to authenticate to the SoftLayer customer portal with.|
|password| string| Your SoftLayer customer portal user's portal password.|
|securityQuestionId| integer| A security question you wish to answer when authenticating to the SoftLayer customer portal. This parameter isn't required if no security questions are set on your portal account or if your account is configured to not require answering a security account upon login.|
|securityQuestionAnswer| string| The answer to your security question.|


### Required Headers


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_User_Customer_Portal_Token'>SoftLayer_Container_User_Customer_Portal_Token </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception "Invalid login credentials provided." if the given username and password combination is incorrect. 

* SoftLayer_Exception_Public 

> Throws the exception "Account has been locked for 30 minutes." if there have been at least ten unsuccessful login attempts for the given username in the past 30 minutes. 

* SoftLayer_Exception_Public 

> Throws the exception "Account has been locked for 30 minutes." if there have been at least ten unsuccessful login attempts from the IP address making the API call in the past 30 minutes. 

* SoftLayer_Exception_Public 

> Throws the exception "Invalid answer provided for security question." if the given security question and answer are invalid and the user is required to answer security questions on portal login. 

* SoftLayer_Exception_Public 

> Throws the exception "Unauthorized IP Address!" if the given user has an IP whitelist defined and the IP address of the user making the api call is not within this user's IP address whitelist. 

* SoftLayer_Exception_Public 

> Throws the exception "Unauthorized IP Address!" if the given user has an IP blacklist defined and the IP address of the user making the api call is within this user's IP address blacklist. 

* SoftLayer_Exception_Public 

> Throws the exception "User account is currently {state}" if the given user is not an active portal user account. In this case {state} contains the current state of the given user account. 




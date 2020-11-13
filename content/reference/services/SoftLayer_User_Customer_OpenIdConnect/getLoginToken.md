---
title: "getLoginToken"
description: "Attempt to authenticate a user to the SoftLayer customer portal using the provided authentication container. Depending o... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/getLoginToken"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::getLoginToken

Authenticate a user for the SoftLayer customer portal


## Overview 
Attempt to authenticate a user to the SoftLayer customer portal using the provided authentication container. Depending on the specific type of authentication container that is used, this API will leverage the appropriate authentication protocol. If authentication is successful then the API returns a list of linked accounts for the user, a token containing the ID of the authenticated user and a hash key used by the SoftLayer customer portal to maintain authentication. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|request| <a href='/reference/datatypes/SoftLayer_Container_Authentication_Request_Contract'>SoftLayer_Container_Authentication_Request_Contract </a>| Container structure that encapsulates data specific to a particular authentication protocol.|


### Required Headers


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Authentication_Response_Common'>SoftLayer_Container_Authentication_Response_Common </a>



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




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
---
# SoftLayer_User_Customer_OpenIdConnect::getLoginToken
## Overview 
Attempt to authenticate a user to the SoftLayer customer portal using the provided authentication container. Depending on the specific type of authentication container that is used, this API will leverage the appropriate authentication protocol. If authentication is successful then the API returns a list of linked accounts for the user, a token containing the ID of the authenticated user and a hash key used by the SoftLayer customer portal to maintain authentication. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|request| <a href='/reference/datatypes/SoftLayer_Container_Authentication_Request_Contract'>SoftLayer_Container_Authentication_Request_Contract </a>| Container structure that encapsulates data specific to a particular authentication protocol.|


### Required Headers

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Authentication_Response_Common'>SoftLayer_Container_Authentication_Response_Common </a>


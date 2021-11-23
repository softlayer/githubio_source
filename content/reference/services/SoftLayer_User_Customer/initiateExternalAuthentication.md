---
title: "initiateExternalAuthentication"
description: "The service initiates an external authentication with the given external authentication vendor. The authentication container and its content will be verified before an attempt is made to initiate an external authentication. [[SoftLayer_Container_User_Customer_External_Binding_Phone|Phone external binding]] container can be used for this service. 

This service returns a unique authentication request token. You can use [[SoftLayer_User_Customer::checkExternalAuthenticationStatus|checkExternalAuthenticationStatus]] service to check if the authentication request is complete or not. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "initiateExternalAuthentication"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer"
---

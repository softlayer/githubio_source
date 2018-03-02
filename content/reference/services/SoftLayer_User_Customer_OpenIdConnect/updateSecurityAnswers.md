---
title: "updateSecurityAnswers"
description: "Update a user's login security questions and answers on the SoftLayer customer portal. These questions and answers are u... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# SoftLayer_User_Customer_OpenIdConnect::updateSecurityAnswers
## Overview 
Update a user's login security questions and answers on the SoftLayer customer portal. These questions and answers are used to optionally log into the SoftLayer customer portal using two-factor authentication. Each user must have three distinct questions set with a unique answer for each question, and each answer may only contain alphanumeric or the . , - _ ( ) [ ] : ; > < characters. Existing user security questions and answers are deleted before new ones are set, and users may only update their own security questions and answers. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|questions| <a href='/reference/datatypes/SoftLayer_User_Security_Question'>SoftLayer_User_Security_Question[] </a>| A list of security questions to use when logging into the SoftLayer customer portal. Each of these objects must have at least their id property populated.|
|answers| array of strings| The answers that correspond to the given list of security questions.|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters

### Optional Headers

### Return Values
boolean


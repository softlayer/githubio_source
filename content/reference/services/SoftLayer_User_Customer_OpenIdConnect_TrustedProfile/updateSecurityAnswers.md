---
title: "updateSecurityAnswers"
description: "Update a user's login security questions and answers on the SoftLayer customer portal. These questions and answers are u... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/updateSecurityAnswers"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::updateSecurityAnswers

Update portal login security questions and answers.


## Overview 
Update a user's login security questions and answers on the SoftLayer customer portal. These questions and answers are used to optionally log into the SoftLayer customer portal using two-factor authentication. Each user must have three distinct questions set with a unique answer for each question, and each answer may only contain alphanumeric or the . , - _ ( ) [ ] : ; > < characters. Existing user security questions and answers are deleted before new ones are set, and users may only update their own security questions and answers. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|questions| <a href='/reference/datatypes/SoftLayer_User_Security_Question'>SoftLayer_User_Security_Question[] </a>| A list of security questions to use when logging into the SoftLayer customer portal. Each of these objects must have at least their id property populated.|
|answers| array of strings| The answers that correspond to the given list of security questions.|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'Access is denied.' if a user tries to change another user's portal login security questions and answers. 

* SoftLayer_Exception_Public 

> Throws the exception 'Please provide three different security questions.' if the questions parameter does not contain three distinct security questions. 

* SoftLayer_Exception_Public 

> Throws the exception 'Please provide three unique security question answers.' if the answers parameter does not contain three unique answers. 

* SoftLayer_Exception_Public 

> Throws the exception ''Please provide valid security questions.' if any of the given security questions do not exist. 




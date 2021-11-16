---
title: "getManagerPreview"
description: "After validating the requesting user through the access token, generates a container with the relevant request informati... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Internal_Ibm"
aliases:
    - "/reference/services/softlayer_account_internal_ibm/getManagerPreview"
---
# [SoftLayer_Account_Internal_Ibm](/reference/services/SoftLayer_Account_Internal_Ibm)::getManagerPreview


Gets a container representing the pending request


## Overview 
After validating the requesting user through the access token, generates a container with the relevant request information and returns it. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|requestId| integer| |
|accessToken| string| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Account_Internal_Ibm_Request'>SoftLayer_Container_Account_Internal_Ibm_Request </a>





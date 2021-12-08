---
title: "activatePartner"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/activatePartner"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::activatePartner


This service enables a partner account that has been created but is currently inactive. This restricted service is only available for certain accounts. Please contact support for questions. 


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|accountId| string| Specify the account ID that needs to be activated.|
|hashCode| string| Specify the hashcode for the partner|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_AccountObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>





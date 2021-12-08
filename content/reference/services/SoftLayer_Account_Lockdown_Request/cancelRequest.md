---
title: "cancelRequest"
description: "Will cancel a lockdown request scheduled in the future. Once canceled, the lockdown request cannot be reconciled and new... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Lockdown_Request"
aliases:
    - "/reference/services/softlayer_account_lockdown_request/cancelRequest"
---
# [SoftLayer_Account_Lockdown_Request](/reference/services/SoftLayer_Account_Lockdown_Request)::cancelRequest


Allows approved brands to cancel a previously scheduled lockdown request.


## Overview 
Will cancel a lockdown request scheduled in the future. Once canceled, the lockdown request cannot be reconciled and new requests must be made for subsequent actions on the account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Account_Lockdown_RequestInitParameters


### Return Values
* void





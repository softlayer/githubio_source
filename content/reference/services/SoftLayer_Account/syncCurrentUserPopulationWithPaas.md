---
title: "syncCurrentUserPopulationWithPaas"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/syncCurrentUserPopulationWithPaas"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::syncCurrentUserPopulationWithPaas

This method manually starts a synchronize operation for the current IBMid-authenticated user population of a linked account pair. "Manually" means "independent of an account link operation". 


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|skipIbmidLookupFlag| boolean| True if we decide to skip IBMid lookup during user sync, False otherwise. (optional)|


### Required Headers
* authenticate


### Return Values
* void



### Error Handling

* Throws 

> SoftLayer_Exception_Public, 'Only Employees or Account master users may manually sync existing user populations.', if the active user is not an Employee or the master user of the account. 

* Throws 

> SoftLayer_Exception_Public, 'Account must be linked before user population can be synced.', if the account attempting to be synced is not linked. 

* Throws 

> SoftLayer_Exception_Public, 'There was an error syncing users in this account.', if an error is encountered during the execution of the user sync 




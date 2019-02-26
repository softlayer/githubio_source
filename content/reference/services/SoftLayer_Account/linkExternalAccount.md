---
title: "linkExternalAccount"
description: "This method will link this SoftLayer account with the provided external account."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/linkExternalAccount"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::linkExternalAccount

This method will link this SoftLayer account with the provided external account. 


## Overview 
This method will link this SoftLayer account with the provided external account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|externalAccountId| string| The ID of the external account to link to this SoftLayer account|
|authorizationToken| string| Access token for any authorization that needs to happen|
|externalServiceProviderKey| string| Key name of the service provider|


### Required Headers
* authenticate


### Return Values
* void



### Error Handling

* Throws 

> SoftLayer_Exception_Public if a link between either of the accounts already exists. 

* Throws 

> SoftLayer_Exception_Public, 'Unable to authenticate request.' if authentication of the request fails. 

* Throws 

> SoftLayer_Exception_Public, 'Unable to link external account to SoftLayer account.', if the attempt to link the accounts fails. 



